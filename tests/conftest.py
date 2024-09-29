import json
import pathlib

import pytest

from httpx import AsyncClient
from psycopg_pool import AsyncConnectionPool

from app.config import settings as global_settings
from app.database import engine
from app.main import app
from app.models.base import Base


@pytest.fixture(
    scope="session",
    params=[
        pytest.param(("asyncio", {"use_uvloop": True}), id="asyncio+uvloop"),
    ],
)
def anyio_backend(request):
    return request.param


@pytest.fixture(scope="session")
async def start_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all, checkfirst=True)
        await conn.run_sync(Base.metadata.create_all, checkfirst=True)
    # for AsyncEngine created in function scope, close and
    # clean-up pooled connections
    await engine.dispose()


@pytest.fixture(scope="session")
async def client(start_db) -> AsyncClient:
    async with AsyncClient(
        app=app,
        base_url="http://testserver/v1",
        headers={"Content-Type": "application/json"},
    ) as test_client:
        _conninfo = global_settings.get_conn_str()
        app.async_pool = AsyncConnectionPool(conninfo=_conninfo)
        yield test_client
        await app.async_pool.close()
