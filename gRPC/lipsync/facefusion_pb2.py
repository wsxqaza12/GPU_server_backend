# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: facefusion.proto
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
    'facefusion.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x66\x61\x63\x65\x66usion.proto\x12\nfacefusion\"S\n\x11\x46\x61\x63\x65\x46usionRequest\x12\x14\n\x0csource_paths\x18\x01 \x03(\t\x12\x13\n\x0btarget_path\x18\x02 \x01(\t\x12\x13\n\x0boutput_path\x18\x03 \x01(\t\"6\n\x12\x46\x61\x63\x65\x46usionResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t2^\n\nFaceFusion\x12P\n\rRunFaceFusion\x12\x1d.facefusion.FaceFusionRequest\x1a\x1e.facefusion.FaceFusionResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'facefusion_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_FACEFUSIONREQUEST']._serialized_start=32
  _globals['_FACEFUSIONREQUEST']._serialized_end=115
  _globals['_FACEFUSIONRESPONSE']._serialized_start=117
  _globals['_FACEFUSIONRESPONSE']._serialized_end=171
  _globals['_FACEFUSION']._serialized_start=173
  _globals['_FACEFUSION']._serialized_end=267
# @@protoc_insertion_point(module_scope)
