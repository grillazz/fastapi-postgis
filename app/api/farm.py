from typing import Union
from uuid import UUID

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

router = APIRouter(prefix="/v1/farm")


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
