from typing import Optional
from uuid import UUID

from geojson_pydantic import Polygon
from pydantic import BaseModel, Field, ConfigDict

config = ConfigDict(
    from_attributes=True,
    extra="ignore",
    json_schema_extra={
        "examples": [
            {
                "name": "Coffe Field 1",
                "description": "This is a coffee field. Cultivation of bourbon grapes.",
                "coordinates": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [28.965931011390687, 53.72790740955463],
                            [28.028874469947816, 51.2464554789114],
                            [32.491115404319764, 50.917482530795894],
                            [28.965931011390687, 53.72790740955463],
                        ]
                    ],
                },
            }
        ]
    },
)

model_config = {
    "json_schema_extra": {
        "examples": [
            {
                "name": "Foo",
                "description": "A very nice Item",
                "price": 35.4,
                "tax": 3.2,
            }
        ]
    }
}


class FarmField(BaseModel):
    model_config = config
    coordinates: Polygon
    name: Optional[str] = Field(None)
    description: Optional[str] = Field(None)


class FarmFieldResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        extra="ignore",
    )
    uuid: UUID
    name: Optional[str]
    description: Optional[str]
    datetime_created: Optional[str]
    datetime_modified: Optional[str]
    area: Optional[float]
    perimeter: Optional[float]
    geojson_coordinates: Optional[str]
