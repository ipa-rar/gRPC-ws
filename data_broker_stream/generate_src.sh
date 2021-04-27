#!/bin/sh
#Modify the PROTO name based on your application
echo "Enter gRPC proto filename"
read filename
PROTO=$filename
#Fixed template 
DIR="generated"
CLIENT=client.py
SERVER=server.py
PROTOFILE=$PROTO.proto

generate_grpc()
{
    python3 -m grpc_tools.protoc \
            --proto_path=. ./$PROTOFILE \
            --python_out=./$DIR \
            --grpc_python_out=./$DIR
}

if [ -d "$DIR" ]; 
then
    mkdir -p $DIR
    generate_grpc
    echo "generated boilerplate files"
else
    rm -Rf $DIR/;
    mkdir -p $DIR
    generate_grpc
    echo "generated boilerplate files"
fi

# modify the lib import 
if test -f $DIR/$PROTO"_pb2_grpc.py"; 
then
    sed -e "5s/.*/from generated import "$PROTO"_pb2 as "$PROTO"__pb2/" -i  $DIR/$PROTO"_pb2_grpc.py"
fi

if test -f "$CLIENT"; 
then
    echo "$CLIENT exists."
else
    touch client.py
    echo "$CLIENT created."
fi

if test -f "$SERVER"; 
then
    echo "$SERVER exists."
else
    touch server.py
    echo "$SERVER created."
fi
