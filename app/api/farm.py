from uuid import UUID

import psycopg
from fastapi import APIRouter, Depends, Request, HTTPException
from fastapi.exceptions import ResponseValidationError
from pydantic import ValidationError
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db

from app.models.farm import FarmField
from app.schemas.farm import FarmFieldResponse, FarmField as FarmFieldSchema

from fastapi import status

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
    response_model=FarmFieldResponse,
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
                if _result is None:
                    raise HTTPException(
                        status_code=status.HTTP_404_NOT_FOUND,
                        detail={
                            "Record not found": f"There is no record for requested name value : {uuid}"
                        },
                    )
                else:
                    return _result
            except (SQLAlchemyError, HTTPException) as ex:
                logger.debug(f"Error: {ex}")
                raise HTTPException(
                    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=repr(ex)
                ) from ex
