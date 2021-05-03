import grpc

from generated import msg_pb2_grpc as Client
from generated import msg_pb2_grpc as msg

from google.protobuf import empty_pb2

port = 'localhost:8061'

class DataBrokerStub():
    
    def __init__(self):
        self.port = 'localhost:8061'
        print(" Client connected on port :"+str(self.port))
        self.channel = grpc.insecure_channel(self.port)
        self.stub = Client.DataBrokerStub(self.channel)
        self.request = empty_pb2.Empty()

    def stream_request(self):
        rows = self.stub.DataBroker(self.request)
        for row in rows:
            print(row)
         
def main():
    client = DataBrokerStub()
    server_reply = client.stream_request()
    
if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted!")
        exit(0)