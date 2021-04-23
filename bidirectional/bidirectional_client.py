from __future__ import print_function

import grpc
from generated import bidirectional_pb2_grpc as bidirectional_pb2_grpc
from generated import bidirectional_pb2 as bidirectional_pb2

def generate_messages():
    messages = [
        bidirectional_pb2.Message("First message"),
        bidirectional_pb2.Message("Second message"),
        bidirectional_pb2.Message("Third message"),
    ]
    for msg in messages:
        print("Hello Server Sending you the %s" % msg.message)
        yield msg


def send_message(stub):
    responses = stub.GetServerResponse(generate_messages())
    for response in responses:
        print("Hello from the server received your %s" % response.message)


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = bidirectional_pb2_grpc.BidirectionalStub(channel)
        send_message(stub)


if __name__ == '__main__':
    run()