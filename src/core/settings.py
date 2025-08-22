from os.path import dirname, join, realpath

from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings


class PostgresSettings(BaseModel):
    """Класс для управления настройками приложения"""

    HOST: str = Field(default="localhost")
    PORT: int = Field(default=5436)
    DB: str = Field(default="docker")
    USER: str = Field(default="docker")
    PASSWORD: str = Field(default="docker")

    @property
    def db_url(self) -> str:
        return (
            f"postgresql+psycopg://{self.USER}:{self.PASSWORD}"
            f"@{self.HOST}:{self.PORT}/{self.DB}"
        )


class Settings(BaseSettings):
    """Механизм для управления настройкам приложения"""

    POSTGRES_SETTINGS: PostgresSettings = PostgresSettings()


def get_settings() -> Settings:

    config_path = join(dirname(realpath(__file__)), "../../settings.json")
    return Settings.parse_file(config_path)
