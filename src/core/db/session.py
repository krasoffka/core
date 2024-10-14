from contextlib import asynccontextmanager
from typing import AsyncGenerator
from uuid import uuid4

from asyncpg import Connection as AsyncpgConnection
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.pool import NullPool
from testcontainers.postgres import PostgresContainer

from core.settings import settings


# https://github.com/sqlalchemy/sqlalchemy/issues/6467
class CustomisedAsyncpgConnection(AsyncpgConnection):
    def _get_unique_id(self, prefix: str) -> str:
        return f'__asyncpg_{prefix}_{uuid4()}__'


db_url = settings.DATABASE_URL
echo = settings.DATABASE_ECHO_MODE
if settings.TEST_DB_MODE == 'TESTCONTAINERS':
    container = PostgresContainer('postgres:16')
    container.start()
    db_url = container.get_connection_url(driver='asyncpg')
elif settings.TEST_DB_MODE == 'LOCAL_DB':
    pass
else:
    raise ValueError('Invalid TEST_DB_MODE value')


engine: AsyncEngine = create_async_engine(
    db_url,
    connect_args={
        'connection_class': CustomisedAsyncpgConnection,
        'prepared_statement_cache_size': 0,
        'statement_cache_size': 0,
        'server_settings': {
            'application_name': settings.SERVICE_NAME,
            'jit': 'off',
        },
    },
    poolclass=NullPool,  # можно добавить пул
    echo=echo,
)

db_session_maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


@asynccontextmanager
async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with db_session_maker() as session:
        async with session.begin():
            try:
                yield session
            except Exception as e:
                # logger.warning(f"Rolling back transaction (due exception={e})")
                raise e
