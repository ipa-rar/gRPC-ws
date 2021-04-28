import grpc
import time

from generated import broker_pb2 as msg
from generated import broker_pb2_grpc as Client
port = 'localhost:50051'

def bidirectional_streaming(stub):

    def request_messages():  
        request = msg.BrokerRequest( id= 14,
        sensor1 = 25.5697,
        sensor2 = 34.6544,
        sensor3 = 58.8795,
        sensor4 = 23.5690)
        yield request
        time.sleep(.1)
    
    response_iterator = stub.BidirectionalStreaming(request_messages())
    
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

        
""" response = msg.Features()
        total_rows = row_obj.init_count()
        current_row = row_obj.current_row
        if(row_obj.current_row < total_rows):
            row = row_obj.get_next_row(current_row)
            response.id = row[0]
            response.sensor1 = row[1]
            response.sensor2 = row[2]
            response.sensor3 = row[3]
            response.sensor4 = row[4]
            row_obj.current_row = row_obj.current_row + 1

        return response """