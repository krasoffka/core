import pytest

from core.grpc_server.proto.core_service_pb2 import TestRequest


@pytest.mark.asyncio(loop_scope='function')
async def test_stub1(stub) -> None:
    await stub.Test(TestRequest(x=1))
    assert True


#
# @pytest.mark.asyncio(loop_scope='function')
# async def test_stub2(stub) -> None:
#     await stub.Test(TestRequest(x=1))
#     assert True
