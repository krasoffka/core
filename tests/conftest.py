import asyncio
import logging

import grpc
import pytest
import pytest_asyncio

from core.db.orm_models import BaseTableORM
from core.db.session import engine, get_async_session
from core.grpc_server.proto.core_service_pb2 import TestRequest
from core.grpc_server.proto.core_service_pb2_grpc import CoreServiceStub
from core.grpc_server.server import init_grpc_server
from core.settings import settings

logger = logging.getLogger(__name__)


@pytest_asyncio.fixture(scope='session', loop_scope='session', autouse=True)
async def setup_db():
    # logger.info("Install test database")
    print('Install test database')
    async with engine.begin() as conn:
        await conn.run_sync(BaseTableORM.metadata.drop_all)
        await conn.run_sync(BaseTableORM.metadata.create_all)


@pytest_asyncio.fixture(scope='function', loop_scope='function')
async def session():
    async with get_async_session() as session:
        yield session


@pytest_asyncio.fixture(scope='session', loop_scope='session', autouse=True)
async def grpc_server():
    async def serve() -> None:
        server = await init_grpc_server()
        await server.start()
        await server.wait_for_termination()

    server_task = asyncio.create_task(serve())
    print(f'Starting grpc server on port {settings.GRPC_SERVICE_PORT}')
    yield
    server_task.cancel()


@pytest_asyncio.fixture(scope='session', loop_scope='session')
async def stub():
    async with grpc.aio.insecure_channel(f'localhost:{settings.GRPC_SERVICE_PORT}') as channel:
        yield CoreServiceStub(channel)
