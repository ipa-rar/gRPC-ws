from generated import stream_msg_pb2_grpc as Server
from generated import stream_msg_pb2 as msg

import grpc
from concurrent import futures

class StreamDataBrokerServicer(Server.StreamDataBrokerServicer):
    def StreamDataBroker:
        

def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Server.add_StreamDataBrokerServicer_to_server(StreamDataBrokerServicer(), server)

if __name__=='__main__':
    main()