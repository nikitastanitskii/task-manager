from typing import AsyncIterator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from src.core.settings import get_settings


class Base(DeclarativeBase):
    """Базовый класс для моделей"""


engine = create_async_engine(
    url=get_settings().POSTGRES_SETTINGS.db_url, echo=True
)


async def get_session() -> AsyncIterator[AsyncSession]:
    """Асинхронное подключение"""
    session_maker = async_sessionmaker(
        autocommit=False, bind=engine, expire_on_commit=False
    )
    async with session_maker() as session:
        yield session
