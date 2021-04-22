#### Once we are done with the creation of the .proto file, we need to generate the stubs.
`````
python3 -m grpc_tools.protoc --proto_path=. ./unary.proto --python_out=. --grpc_python_out=.
`````

[Reference](https://www.velotio.com/engineering-blog/grpc-implementation-using-python)