from core.grpc_server.proto import core_service_pb2 as client_pb
from core.settings import settings


class CoreServiceGrpc:
    # @antifraud_exception_handler(client_pb.TemporaryBlockRequisiteResponse)
    async def Test(self, request: client_pb.TestRequest, context) -> client_pb.TestResponse:
        print(f'Получен запрос с x={request.x}')  # Лог на сервере
        return client_pb.TestResponse(result='OK')
