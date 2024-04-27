from pydantic import PostgresDsn, computed_field
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
            scheme="postgresql+psycopg",
            username=self.SQL_USER,
            password=self.SQL_PASSWORD,
            host=self.SQL_HOST,
            path=self.SQL_DB,
        )

    def get_conn_str(self):
        return f"dbname={self.SQL_DB} user={self.SQL_USER} password={self.SQL_PASSWORD} host={self.SQL_HOST} port=5432"


settings = Settings()
