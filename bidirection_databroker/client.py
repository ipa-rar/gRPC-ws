import time
import csv
import grpc

from generated import broker_pb2 as msg
from generated import broker_pb2_grpc as Client
PORT = 'localhost:8061'
STREAM_RATE  = 0.01


def bidirectional_streaming(stub):

    def stream_messages():
        """Server request callback function"""
        csv_filename = "./dataset/sensors.csv"
        with open(csv_filename, "r") as dataset:
            row = csv.reader(dataset, delimiter=",")
            for i, data in enumerate(row):
                request = msg.BrokerRequest(id=int(data[0]),
                                            sensor1=float(data[1]),
                                            sensor2=float(data[2]),
                                            sensor3=float(data[3]),
                                            sensor4=float(data[4]))
                yield request
                time.sleep(STREAM_RATE)

    response_iterator = stub.BidirectionalStreaming(stream_messages())

    for response in response_iterator:
        print("Server response: ", int(response.id), bool(response.prediction))


def main():
    with grpc.insecure_channel(PORT) as channel:
        stub = Client.BrokerServiceStub(channel)
        bidirectional_streaming(stub)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted!")
        exit(0)
