# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: io/cloudevents/example/service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from io.cloudevents.v1 import cloudevents_pb2 as io_dot_cloudevents_dot_v1_dot_cloudevents__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$io/cloudevents/example/service.proto\x12\x16io.cloudevents.example\x1a#io/cloudevents/v1/cloudevents.proto2R\n\x07Greeter\x12G\n\x05hello\x12\x1d.io.cloudevents.v1.CloudEvent\x1a\x1d.io.cloudevents.v1.CloudEvent\"\x00\x42\xa4\x01\n\x1cio.cloudevents.example.protoP\x01Z\x1f\x63loudevents.io/genproto/example\xaa\x02\x1f\x43loudNative.CloudEvents.Example\xca\x02\x1cIo\\CloudEvents\\Example\\Proto\xea\x02\x1fIo::CloudEvents::Example::Protob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'io.cloudevents.example.service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\034io.cloudevents.example.protoP\001Z\037cloudevents.io/genproto/example\252\002\037CloudNative.CloudEvents.Example\312\002\034Io\\CloudEvents\\Example\\Proto\352\002\037Io::CloudEvents::Example::Proto'
  _GREETER._serialized_start=101
  _GREETER._serialized_end=183
# @@protoc_insertion_point(module_scope)