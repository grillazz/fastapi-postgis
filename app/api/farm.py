from typing import Union
from uuid import UUID

import psycopg
from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession
from geojson_pydantic import Polygon
from geoalchemy2.shape import to_shape
from geoalchemy2.functions import ST_Area

from app.database import get_db

from app.models.farm import FarmField
from app.schemas.farm import FarmFieldResponse, FarmField as FarmFieldSchema

from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError

from app.utils.logging import AppLogger

router = APIRouter(prefix="/v1/farm")

logger = AppLogger().get_logger()


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    response_model=FarmFieldResponse,
)
async def create_field(
    payload: FarmFieldSchema,
    db_session: AsyncSession = Depends(get_db),
):
    farm_field = FarmField(
        name=payload.name,
        description=payload.description,
        coordinates=f"SRID=4326;{payload.coordinates.wkt}",
    )
    await farm_field.save_and_refresh(db_session)

    return farm_field


@router.get(
    "/{uuid}",
    # response_model=FarmFieldResponse,
)
async def get_field(
    uuid: UUID,
    request: Request,
):

    _sql = await FarmField.get_farm_fields(
        where_conditions=[FarmField.uuid == uuid], compile_sql=True
    )

    async with request.app.async_pool.connection() as conn:
        async with conn.cursor(row_factory=psycopg.rows.dict_row) as cur:

            try:
                await cur.execute(str(_sql))
                _result = await cur.fetchone()
                # TODO: pydantic model for response like https://blog.dalibo.com/2022/06/01/psycopg-row-factories.html

                logger.debug(f"SQL: {_sql}")
                logger.debug(f"Result: {_result}")

                return _result
            except Exception as e:
                logger.debug(f"Error: {e}")
                return {"error": f"Error: {e}"}
