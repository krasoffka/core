from core.grpc_server.proto import service_pb2 as client_pb


class CoreServiceGrpc:
    # @antifraud_exception_handler(client_pb.TemporaryBlockRequisiteResponse)
    async def Test(self, request: client_pb.TestRequest, context) -> client_pb.TestResponse:
        return client_pb.TestResponse()
