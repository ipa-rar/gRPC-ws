import grpc
from concurrent import futures

from generated import sensor_msgs_pb2_grpc as Server
from generated import sensor_msgs_pb2 as msg
port = 8061

class FaultDetectionServicer(Server.FaultDetectionServicer):
    def get_features(self, request, context):
        


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
Server.add_FaultDetectionServicer_to_server(FaultDetectionServicer(),server)

Print("Starting server. Listening on port : " + str(port))
server.add_insecure_port("[::]:{}".format(port))
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)


