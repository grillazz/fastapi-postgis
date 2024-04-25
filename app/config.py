import os

from pydantic import PostgresDsn, RedisDsn, computed_field
from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="fram.env", env_ignore_empty=True, extra="ignore"
    )

    SQL_USER: str
    SQL_PASSWORD: str
    SQL_HOST: str
    SQL_DB: str

    @computed_field
    @property
    def sql_url(self) -> PostgresDsn:
        return MultiHostUrl.build(
            scheme="postgresql+asyncpg",
            username=self.SQL_USER,
            password=self.SQL_PASSWORD,
            host=self.SQL_HOST,
            path=self.SQL_DB,
        )


settings = Settings()
