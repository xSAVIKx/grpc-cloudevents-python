# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from cloudevents.v1 import cloudevents_pb2 as io_dot_cloudevents_dot_v1_dot_cloudevents__pb2


class GreeterStub(object):
    """The greeting service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.hello = channel.unary_unary(
                '/io.cloudevents.example.Greeter/hello',
                request_serializer=io_dot_cloudevents_dot_v1_dot_cloudevents__pb2.CloudEvent.SerializeToString,
                response_deserializer=io_dot_cloudevents_dot_v1_dot_cloudevents__pb2.CloudEvent.FromString,
                )


class GreeterServicer(object):
    """The greeting service definition.
    """

    def hello(self, request, context):
        """Sends a greeting
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GreeterServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'hello': grpc.unary_unary_rpc_method_handler(
                    servicer.hello,
                    request_deserializer=io_dot_cloudevents_dot_v1_dot_cloudevents__pb2.CloudEvent.FromString,
                    response_serializer=io_dot_cloudevents_dot_v1_dot_cloudevents__pb2.CloudEvent.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'io.cloudevents.example.Greeter', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Greeter(object):
    """The greeting service definition.
    """

    @staticmethod
    def hello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/io.cloudevents.example.Greeter/hello',
            io_dot_cloudevents_dot_v1_dot_cloudevents__pb2.CloudEvent.SerializeToString,
            io_dot_cloudevents_dot_v1_dot_cloudevents__pb2.CloudEvent.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)