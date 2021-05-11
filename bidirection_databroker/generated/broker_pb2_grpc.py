# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from generated import broker_pb2 as broker__pb2


class BrokerServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.BidirectionalStreaming = channel.stream_stream(
                '/bidirectional_databroker.BrokerService/BidirectionalStreaming',
                request_serializer=broker__pb2.BrokerRequest.SerializeToString,
                response_deserializer=broker__pb2.BrokerResponse.FromString,
                )


class BrokerServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def BidirectionalStreaming(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BrokerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'BidirectionalStreaming': grpc.stream_stream_rpc_method_handler(
                    servicer.BidirectionalStreaming,
                    request_deserializer=broker__pb2.BrokerRequest.FromString,
                    response_serializer=broker__pb2.BrokerResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'bidirectional_databroker.BrokerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class BrokerService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def BidirectionalStreaming(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/bidirectional_databroker.BrokerService/BidirectionalStreaming',
            broker__pb2.BrokerRequest.SerializeToString,
            broker__pb2.BrokerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)