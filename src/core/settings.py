import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SERVICE_NAME = "core_service"
    GRPC_SERVICE_PORT: int = 8181

    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@127.0.0.1:5432/core"
    # база данных для тестов, установить свою, если необходимо. Перезатирается при тестах!!!
    DATABASE_TEST_URL = "postgresql+asyncpg://postgres:postgres@127.0.0.1:5432/core_test"
    DATABASE_ECHO_MODE: bool = False
    DATABASE_TEST_ECHO_MODE: bool = False

    JSON_LOGS: bool = True
    DEBUG: bool = False

    class Config:
        env_file = os.environ.get("ENV_FILE_PATH", ".env")


settings = Settings()
