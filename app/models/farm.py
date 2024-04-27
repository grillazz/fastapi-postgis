import uuid
from datetime import datetime
from typing import Any, Optional

from geoalchemy2 import Geometry, WKBElement
from geoalchemy2.functions import ST_Area, ST_Perimeter, ST_AsGeoJSON
from sqlalchemy import (
    Column,
    String,
    DateTime,
    Boolean,
    Float,
    ForeignKey,
    select,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class FarmField(Base):
    __tablename__ = "farm_field"
    __table_args__ = ({"schema": "coffee"},)
    uuid = Column(
        UUID(as_uuid=True),
        unique=True,
        default=uuid.uuid4,
        primary_key=True,
    )
    coordinates = Column(Geometry("POLYGON", srid=4326), nullable=False)

    datetime_created: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=datetime.now()
    )
    datetime_modified: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=datetime.now(), onupdate=datetime.now()
    )
    name: Mapped[Optional[str]]
    description: Mapped[Optional[str]]

    @classmethod
    async def get_farm_fields(
        cls, database_session: AsyncSession, where_conditions: list[Any], compile_sql: bool = False
    ):
        _stmt = select(
            cls,
            ST_Area(cls.coordinates, True).label("area"),
            ST_Perimeter(cls.coordinates, True).label("perimeter"),
            ST_AsGeoJSON(cls.coordinates).label("geojson_coordinates"),
        ).where(*where_conditions)

        if compile_sql:
            return _stmt.compile(compile_kwargs={"literal_binds": True})

        _result = await database_session.execute(_stmt)
        return _result.fetchall()
