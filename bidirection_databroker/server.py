from concurrent import futures
from threading import Thread
import logging
import grpc

from generated import broker_pb2 as msg
from generated import broker_pb2_grpc as Server
PORT = 8061


class BrokerServiceServicer(Server.BrokerServiceServicer):

    def __call__(self, request_iterator):
        """Receives the client request stream and process it"""
        for request in request_iterator:
            logging.info("request")
            print(request.id,
                  request.sensor1,
                  request.sensor2,
                  request.sensor3,
                  request.sensor4)
            

    def BidirectionalStreaming(self, request_iterator, context):
        """Server request callback function"""
        process = Thread(target=self, args=(request_iterator,)) 
        process.start()
        yield msg.BrokerResponse(id=15, prediction=True)
        # apply some algorithm here on the received data
        logging.warning("foobar")
        process.join()


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Server.add_BrokerServiceServicer_to_server(BrokerServiceServicer(), server)
    print("Starting server. Listening on port : " + str(PORT))
    server.add_insecure_port("[::]:{}".format(PORT))
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted!")
        exit(0)
