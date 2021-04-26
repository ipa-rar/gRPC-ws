#!/bin/sh

DIR="generated"
PROTO="msg.proto"

run_cmd()
{
    python3 -m grpc_tools.protoc \
            --proto_path=. ./$PROTO \
            --python_out=./$DIR \
            --grpc_python_out=./$DIR
}

if [ -d "$DIR" ]; 
then
    mkdir -p $DIR
    run_cmd
else
    rm -Rf $DIR/;
    mkdir -p $DIR
    run_cmd
fi

