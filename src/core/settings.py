from pathlib import Path

from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings


class PostgresSettings(BaseModel):
    """Класс для управления настройками приложения"""

    HOST: str = Field(default="localhost")
    PORT: int = Field(default=5432)
    DB: str = Field(default="postgres")
    USER: str = Field(default="postgres")
    PASSWORD: str = Field(default="postgres")

    @property
    def db_url(self) -> str:
        return (
            f"postgresql+psycopg://{self.USER}:{self.PASSWORD}"
            f"@{self.HOST}:{self.PORT}/{self.DB}"
        )


class Settings(BaseSettings):
    """Класс для управления настройками приложения"""

    POSTGRES_SETTINGS: PostgresSettings = PostgresSettings()


def get_settings() -> Settings:

    config_path = Path(__file__).resolve().parent.parent.parent / "settings.json"
    return Settings.parse_file(config_path)
