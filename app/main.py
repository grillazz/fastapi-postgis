from contextlib import asynccontextmanager

from fastapi import FastAPI

from psycopg_pool import AsyncConnectionPool

from app.config import settings as global_settings


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

app = FastAPI(title="Farm API", version="0.0.1", lifespan=lifespan)


# TODO print raw sql from sqlalchemy orm and pass it to ppsycopg_pool
# https://medium.com/@benshearlaw/asynchronous-postgres-with-python-fastapi-and-psycopg-3-fafa5faa2c08
# TODO: add decorator to get RAW SQL from current complex ORM query
