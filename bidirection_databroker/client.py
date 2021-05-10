import grpc
import time
import csv

from generated import broker_pb2 as msg
from generated import broker_pb2_grpc as Client
port = 'localhost:8061'

def bidirectional_streaming(stub):

    def request_messages():  
        for i in range(100):
            request = msg.BrokerRequest( id= i,
            sensor1 = i+1.06034923580252875,
            sensor2 = i+2.06034923580252875,
            sensor3 = i+3.06034923580252875,
            sensor4 = i+4.06034923580252875)
            yield request
            time.sleep(.1)

    def stream_messages():
        csv_filename = "./dataset/sensors.csv"
        with open(csv_filename, "r") as dataset:
            row = csv.reader(dataset, delimiter=",")
            for i, data in enumerate(row):
                request = msg.BrokerRequest(id=data[0],
                sensor1=data[1],
                sensor2=data[2],
                sensor3=data[3],
                sensor4=data[4])
                yield request
                time.sleep(.01) 

    
    response_iterator = stub.BidirectionalStreaming(request_messages())
    #response_iterator = stub.BidirectionalStreaming(stream_messages())

    for response in response_iterator:
        print(response.id,
        response.prediction)

def main():
    with grpc.insecure_channel(port) as channel:
        stub = Client.BrokerServiceStub(channel)
        bidirectional_streaming(stub)

if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted!")
        exit(0)

        
