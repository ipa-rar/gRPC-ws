python3 -m grpc_tools.protoc \
        --proto_path=. ./unary.proto \
        --python_out=./generated \
        --grpc_python_out=./generated
