import grpc
from concurrent import futures

from generated import msg_pb2_grpc as Server
from generated import msg_pb2_grpc as msg

from google.protobuf import empty_pb2

port = 'localhost:50051'

def main(port):
    with grpc.insecure_channel(port) as channel:
        stub = model_pb2_grpc.DataBrokerStub(channel)
        request = msg.Empty('')
        nextrow = stub.DataBroker(request)

        print('The next row is :', nextrow)
        print('status of response:', grpc.StatusCode.OK.value)
        for i in grpc.StatusCode:
            print(i, i.value)

if __name__ == '__main__':
    main(port = 'localhost:50051')