from contextlib import asynccontextmanager

from fastapi import FastAPI

from psycopg_pool import AsyncConnectionPool

from app.config import settings as global_settings
from app.api.farm import router as farm_router


@asynccontextmanager
async def lifespan(app: FastAPI):

    _conninfo = global_settings.get_conn_str()
    try:
        # Load the async pool connection
        app.async_pool = AsyncConnectionPool(conninfo=_conninfo)
        yield
    finally:
        # close redis connection and release the resources
        await app.async_pool.close()


app = FastAPI(title="Farm API", version="0.0.3", lifespan=lifespan)

app.include_router(farm_router)


# TODO print raw sql from sqlalchemy orm and pass it to ppsycopg_pool
# https://medium.com/@benshearlaw/asynchronous-postgres-with-python-fastapi-and-psycopg-3-fafa5faa2c08
# TODO: add decorator to get RAW SQL from current complex ORM query
# TODO: analyze codebase describe implementation details for project and make blog post from it
