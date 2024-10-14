# from typing import Any, Callable
#
# import grpc
# from antifraud_service.utils.metrics import METRICS
# from antifraud_service_proto import client_pb2
# from google.protobuf.json_format import MessageToJson
# from grpc_interceptor import AsyncServerInterceptor
# from loguru import logger
#
# ANTIFRAUD_SERVICE_METHODS = [
#     method.name for method in client_pb2.DESCRIPTOR.services_by_name["AntiFraudService"].methods
# ]
#
#
# def _is_service_method(method_full_name: str) -> bool:
#     method_name = method_full_name.split("/")[-1]
#     return method_name in ANTIFRAUD_SERVICE_METHODS
#
#
# class RequestLoggerInterceptor(AsyncServerInterceptor):
#     async def intercept(
#         self,
#         method: Callable[..., Any],
#         request_or_iterator: Any,
#         context: grpc.ServicerContext,
#         method_name: str,
#     ) -> Any:
#         if _is_service_method(method_name):
#             logger.info(f"Received request: {MessageToJson(request_or_iterator)}")
#             result = await super().intercept(method, request_or_iterator, context, method_name)
#             logger.info(f"Response: {MessageToJson(result)}")
#             return result
#         else:
#             return await super().intercept(method, request_or_iterator, context, method_name)
#
#
# class ErrorResponseMetricInterceptor(AsyncServerInterceptor):
#     async def intercept(
#         self,
#         method: Callable[..., Any],
#         request_or_iterator: Any,
#         context: grpc.ServicerContext,
#         method_name: str,
#     ) -> Any:
#         result = await super().intercept(method, request_or_iterator, context, method_name)
#         if hasattr(result, "error") and result.HasField("error") and result.WhichOneof("message") == "error":
#             error = result.error
#             METRICS.error_rate(
#                 action_name=method_name.split("/")[-1] or method_name,
#                 code=error.code,
#                 message=error.message,
#             ).inc()
#
#         return result
