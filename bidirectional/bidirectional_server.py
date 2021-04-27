from concurrent import futures
import grpc

from generated import bidirectional_pb2_grpc as Server
port='[::]:50051'

class BidirectionalService(Server.BidirectionalServicer):

    def GetServerResponse(self, request_iterator, context):
        for message in request_iterator:
            yield message

def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Server.add_BidirectionalServicer_to_server(BidirectionalService(), server)
    server.add_insecure_port(port)
    print("Starting server. Listening on port : " + str(port))
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted!")
        exit(0)