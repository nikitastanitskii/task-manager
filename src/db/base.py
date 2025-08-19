from typing import Iterator
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Session
from sqlalchemy import create_engine

from src.core.settings import get_settings


class Base(DeclarativeBase):
    """Базовый класс для создания моделей"""


engine = create_engine(url=get_settings().POSTGRES_SETTINGS.db_url, echo=True)


def get_session() -> Iterator[Session]:
    """Синхронное подключение"""
    session_maker = sessionmaker(autocommit=False, bind=engine, expire_on_commit=False)
    with session_maker as session:
        yield session
