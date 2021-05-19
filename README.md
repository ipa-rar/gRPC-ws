# gRPC-Workspce
## For implementing gRPC services, we need to define three files:
- **Proto file** Proto file comprises the declaration of the service that is used to generate stubs `(<package_name>_pb2.py and <package_name>_pb2_grpc.py)`. These are used by the gRPC client and the gRPC server.</package_name></package_name>
- **gRPC client** The client makes a gRPC call to the server to get the response as per the proto file.‍
- **gRPC Server** The server is responsible for serving requests to the client.

## Template for creating gRPC projects
For the ease of getting started with gRPC projects I have created a shell script that can be used to generate the boilerplate code, client and server. 
## Steps to use this template
1. Create the proto file 
2. Run the shell script to generate client.py, server.py and generate boiler plate code for gRPC project.
    ````
    sh generate_src.sh
    ````
3. Enter the name of the proto file you have created in step 1.
4. Now, you have all the files to get started with the gRPC project.

**Note: This script works perfectly when proto file names that does not contain `space`, `_` and `-`**

## References
- [Data transmission Client](https://github.com/grpc/grpc/blob/master/examples/python/data_transmission/client.py)
- [Data transmission Server](https://github.com/grpc/grpc/blob/master/examples/python/data_transmission/server.py)
- [Best practices for gRPC microservices](https://realpython.com/python-microservices-grpc/#python-microservice-monitoring-with-interceptors)



