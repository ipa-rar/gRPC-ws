# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from generated import stream_msg_pb2 as stream__msg__pb2


class StreamDataBrokerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StreamDataBroker = channel.stream_stream(
                '/StreamDataBroker/StreamDataBroker',
                request_serializer=stream__msg__pb2.Empty.SerializeToString,
                response_deserializer=stream__msg__pb2.Features.FromString,
                )


class StreamDataBrokerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def StreamDataBroker(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StreamDataBrokerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'StreamDataBroker': grpc.stream_stream_rpc_method_handler(
                    servicer.StreamDataBroker,
                    request_deserializer=stream__msg__pb2.Empty.FromString,
                    response_serializer=stream__msg__pb2.Features.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'StreamDataBroker', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class StreamDataBroker(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def StreamDataBroker(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/StreamDataBroker/StreamDataBroker',
            stream__msg__pb2.Empty.SerializeToString,
            stream__msg__pb2.Features.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)