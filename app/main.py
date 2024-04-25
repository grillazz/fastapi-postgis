from fastapi import FastAPI

app = FastAPI(title="Farm API", version="0.0.1")


# TODO print raw sql from sqlalchemy orm and pass it to ppsycopg_pool
# https://medium.com/@benshearlaw/asynchronous-postgres-with-python-fastapi-and-psycopg-3-fafa5faa2c08
# TODO: add decorator to get RAW SQL from current complex ORM query
