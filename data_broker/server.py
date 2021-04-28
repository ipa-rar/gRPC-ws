import grpc
from concurrent import futures
import time

from generated import msg_pb2_grpc as Server
from generated import msg_pb2 as msg

from data_broker import fetch_csv

row_obj = fetch_csv.FetchRowCSV()
current_row = 0
port = 50051

class DataBrokerServicer(Server.DataBrokerServicer):
    
    def DataBroker(self, request, context):
        response = msg.Features()
        if request:
            total_rows = row_obj.init_count()
            current_row = row_obj.current_row
            for row_obj.current_row in range(total_rows):
                row = row_obj.get_next_row(row_obj.current_row)
                response.id = row[0]
                response.sensor1 = row[1]
                response.sensor2 = row[2]
                response.sensor3 = row[3]
                response.sensor4 = row[4]
                yield response
                time.sleep(0.1)


def main():
    try:
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        Server.add_DataBrokerServicer_to_server(DataBrokerServicer(),server)
        print("Starting server. Listening on port : " + str(port))
        server.add_insecure_port("[::]:{}".format(port))
        server.start()
        server.wait_for_termination()

    except KeyboardInterrupt:
        server.stop(0)

if __name__=='__main__':
    main()


