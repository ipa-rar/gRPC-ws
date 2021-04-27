import grpc
from generated import bidirectional_pb2_grpc as Client
from generated import bidirectional_pb2 as msg

def generate_messages():
    messages = [
        msg.Message(message="1 message"),
        msg.Message(message="2 message"),
        msg.Message(message="3 message"),
        msg.Message(message="4 message"),
        msg.Message(message="5 message"),
        msg.Message(message="6 message"),
        msg.Message(message="7 message"),
        msg.Message(message="8 message"),
        msg.Message(message="9 message"),
    ]
    for msgs in messages:
        print("Hello Server Sending you the %s" % msgs.message)
        yield msgs


def send_message(stub):
    responses = stub.GetServerResponse(generate_messages())
    for response in responses:
        print("Hello from the server received your %s" % response.message)


def main():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = Client.BidirectionalStub(channel)
        send_message(stub)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted!")
        exit(0)