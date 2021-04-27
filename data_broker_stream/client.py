from generated import stream_msg_pb2_grpc as Client
from generated import stream_msg_pb2 as msg

import grpc
from google.protobuf import empty_pb2

class StreamDataBrokerStub():
    
    def __init__(self):
        self.port = 'localhost:50051'
        self.channel = grpc.insecure_channel(self.port)
        self.stub = Client.StreamDataBrokerStub(self.channel)

    def send_request_stream(self):
        request = empty_pb2.Empty()
        responses = self.stub.StreamDataBroker(request)
        for response in responses:
            yield response
        
    
def main():
    client = StreamDataBrokerStub()
    server_result = client.send_request_stream()
    for r in server_result:
        print(r)

if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted!")
        exit(0)

        
