import pytest
from fastapi import status
from httpx import AsyncClient
from dirty_equals import IsDatetime, IsUUID, IsPositiveFloat
from inline_snapshot import snapshot


# Integration tests
pytestmark = pytest.mark.anyio


async def test_create_field(client: AsyncClient):
    response = await client.post(
        "/farm",
        json={
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
        },
    )

    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == snapshot(
        {
            "uuid": IsUUID(4),
            "name": "Coffe Field 1",
            "description": "This is a coffee field. Cultivation of bourbon grapes.",
            "datetime_created": IsDatetime(iso_string=True),
            "datetime_modified": IsDatetime(iso_string=True),
            "area": IsPositiveFloat(),
            "perimeter": IsPositiveFloat(),
            "geojson_coordinates": None,
        }
    )


async def test_get_field(client: AsyncClient):
    response = await client.post(
        "/farm",
        json={
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
        },
    )

    assert response.status_code == status.HTTP_201_CREATED

    response = await client.get(f"/farm/{response.json()['uuid']}")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == snapshot(
        {
            "uuid": IsUUID(4),
            "name": "Coffe Field 1",
            "description": "This is a coffee field. Cultivation of bourbon grapes.",
            "datetime_created": IsDatetime(iso_string=True),
            "datetime_modified": IsDatetime(iso_string=True),
            "area": IsPositiveFloat(),
            "perimeter": IsPositiveFloat(),
            "geojson_coordinates": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [28.965931011, 53.72790741],
                        [28.02887447, 51.246455479],
                        [32.491115404, 50.917482531],
                        [28.965931011, 53.72790741],
                    ]
                ],
            },
        }
    )
