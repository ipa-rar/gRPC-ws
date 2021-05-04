import grpc
from concurrent import futures
from threading import Thread

from generated import broker_pb2 as msg
from generated import broker_pb2_grpc as Server
port = 8061

class BrokerServiceServicer(Server.BrokerServiceServicer):

    def ProcessRequest(self, request_iterator):
        for request in request_iterator:
            print(request.id, 
                request.sensor1,
                request.sensor2,
                request.sensor3,
                request.sensor4)
                
        
    def BidirectionalStreaming(self, request_iterator, context):
        t = Thread(target=self.ProcessRequest(request_iterator))
        t.start()
        ## apply some algorithm here on the received data
        self.ProcessRequest(request_iterator)

        yield msg.BrokerResponse(
            id = 15,
            prediction = True
        )
        t.join()

def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Server.add_BrokerServiceServicer_to_server(BrokerServiceServicer(), server)
    print("Starting server. Listening on port : " + str(port))
    server.add_insecure_port("[::]:{}".format(port))
    server.start()
    server.wait_for_termination()

if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted!")
        exit(0)
