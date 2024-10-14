from pydantic import BaseModel

from core.grpc_server.proto.core_service_pb2 import TestRequest


class Test(BaseModel):
    id: int

    class Config:
        orm_mode = True

    @classmethod
    def from_proto(cls, proto: TestRequest) -> 'Test':
        return cls(id=proto.id)
