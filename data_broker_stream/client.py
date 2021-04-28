from generated import stream_msg_pb2_grpc as Client
from generated import stream_msg_pb2 as msg

import grpc
from google.protobuf import empty_pb2

class StreamDataBrokerStub():
    
    def __init__(self):
        self.port = 'localhost:50051'
        self.channel = grpc.insecure_channel(self.port)
        self.stub = Client.StreamDataBrokerStub(self.channel)
        self.request = empty_pb2.Empty()

    def send_request_stream(self):
        rows = self.stub.StreamDataBroker(self.request)
        for row in rows:
            print(row)

def main():
    client = StreamDataBrokerStub()
    client.send_request_stream()


if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted!")
        exit(0)

        
