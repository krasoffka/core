# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: src/core/grpc_server/proto/core_service.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'src/core/grpc_server/proto/core_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-src/core/grpc_server/proto/core_service.proto\x12\x04\x63ore\"\x18\n\x0bTestRequest\x12\t\n\x01x\x18\x01 \x01(\x05\"\x1e\n\x0cTestResponse\x12\x0e\n\x06result\x18\x01 \x01(\t2<\n\x0b\x43oreService\x12-\n\x04Test\x12\x11.core.TestRequest\x1a\x12.core.TestResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'src.core.grpc_server.proto.core_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_TESTREQUEST']._serialized_start=55
  _globals['_TESTREQUEST']._serialized_end=79
  _globals['_TESTRESPONSE']._serialized_start=81
  _globals['_TESTRESPONSE']._serialized_end=111
  _globals['_CORESERVICE']._serialized_start=113
  _globals['_CORESERVICE']._serialized_end=173
# @@protoc_insertion_point(module_scope)
