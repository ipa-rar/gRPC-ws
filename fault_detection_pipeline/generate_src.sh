python3 -m grpc_tools.protoc \
        --proto_path=. ./sensor_msgs.proto \
        --python_out=./generated \
        --grpc_python_out=./generated
