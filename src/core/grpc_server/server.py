import asyncio

import grpc
from grpc import Server
from grpc_reflection.v1alpha import reflection

import core.grpc_server.proto.core_service_pb2 as service
from core.grpc_server.grpc_servicer import CoreServiceGrpc
from core.grpc_server.proto.core_service_pb2_grpc import add_CoreServiceServicer_to_server
from core.settings import settings

# Coroutines to be invoked when the event loop is shutting down.
_cleanup_coroutines = []


async def init_grpc_server() -> Server:
    interceptors = [
        # RequestLoggerInterceptor(),
        # ErrorResponseMetricInterceptor(),
    ]
    server = grpc.aio.server(interceptors=interceptors)

    add_CoreServiceServicer_to_server(
        CoreServiceGrpc(),
        server,
    )
    service_names = [
        service.DESCRIPTOR.services_by_name['CoreService'].full_name,
        reflection.SERVICE_NAME,
    ]
    reflection.enable_server_reflection(service_names, server)  # type: ignore[arg-type]
    listen_addr = f'[::]:{settings.GRPC_SERVICE_PORT}'
    server.add_insecure_port(listen_addr)
    return server


async def serve() -> None:
    server = await init_grpc_server()
    await server.start()

    print(f'Starting grpc server on port {settings.GRPC_SERVICE_PORT}')

    async def server_graceful_shutdown() -> None:
        # logger.info("Starting graceful shutdown...")
        await server.stop(5)

    _cleanup_coroutines.append(server_graceful_shutdown())
    await server.wait_for_termination()


def run():
    loop = asyncio.new_event_loop()
    try:
        loop.run_until_complete(serve())
    finally:
        loop.run_until_complete(*_cleanup_coroutines)
        loop.close()


if __name__ == '__main__':
    run()
