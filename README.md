# gRPC-Workspce
#### For implementing gRPC services, we need to define three files:
- **Proto file** Proto file comprises the declaration of the service that is used to generate stubs `(<package_name>_pb2.py and <package_name>_pb2_grpc.py)`. These are used by the gRPC client and the gRPC server.</package_name></package_name>
- **gRPC client** The client makes a gRPC call to the server to get the response as per the proto file.‍
- **gRPC Server** The server is responsible for serving requests to the client.

#### Once we are done with the creation of the .proto file, we need to generate the stubs.
`````
python3 -m grpc_tools.protoc --proto_path=. ./hello-world-msg.proto --python_out=./stubs/ --grpc_python_out=./stubs/
`````

