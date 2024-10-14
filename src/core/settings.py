import os
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    SERVICE_NAME: str = 'core_service'
    GRPC_SERVICE_PORT: int = 8181

    DATABASE_URL: str = 'postgresql+asyncpg://postgres:postgres@127.0.0.1:5432/core'
    TEST_DB_MODE: Literal['LOCAL_DB', 'TESTCONTAINERS'] = 'TESTCONTAINERS'
    DATABASE_ECHO_MODE: bool = False

    JSON_LOGS: bool = True
    DEBUG: bool = False
    model_config = SettingsConfigDict(
        env_file=os.environ.get('ENV_FILE_PATH', '.env'),
        extra='allow',
    )


settings = Settings()
