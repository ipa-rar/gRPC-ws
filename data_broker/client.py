import grpc

from generated import msg_pb2_grpc as Client
from generated import msg_pb2_grpc as msg

from google.protobuf import empty_pb2

port = 'localhost:50051'

def main(port):
    with grpc.insecure_channel(port) as channel:
        stub = Client.DataBrokerStub(channel)

        request = empty_pb2.Empty()
        rows = stub.DataBroker(request)
        
        print(rows)

if __name__ == '__main__':
    main(port = 'localhost:50051')