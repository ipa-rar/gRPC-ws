from generated import stream_msg_pb2_grpc as Server
from generated import stream_msg_pb2 as msg

import grpc
from concurrent import futures
port = 50051

import fetch_csv as f
row_obj = f.FetchRowCSV()
current_row = 0

class StreamDataBrokerServicer(Server.StreamDataBrokerServicer):
    
    def fetch_csv(self):
        with open(csv_filename, "r", encoding="latin-1") as dataset:
            for data in csv.reader(dataset):
                yield data
            
    def StreamDataBroker(self, requests, context):
        #csv_filename = "./dataset/sensors.csv"
        response = msg.Features()

        total_rows = row_obj.init_count()
        current_row = row_obj.current_row
        row = row_obj.get_next_row(current_row)
        response.id = row[0]
        response.sensor1 = row[1]
        response.sensor2 = row[2]
        response.sensor3 = row[3]
        response.sensor4 = row[4]
        row_obj.current_row = row_obj.current_row + 1
        
        yield response

def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Server.add_StreamDataBrokerServicer_to_server(StreamDataBrokerServicer(), server)
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