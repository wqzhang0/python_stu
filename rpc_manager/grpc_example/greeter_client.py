from concurrent.futures import ThreadPoolExecutor

import grpc
import time

from rpc_manager.grpc_example import helloworld_pb2_grpc, helloworld_pb2


def run():
    channel = grpc.insecure_channel('localhost:5000')
    stub = helloworld_pb2_grpc.GreeterStub(channel)
    response = stub.SayHello(helloworld_pb2.HelloRequest(name='you'))
    print("Greeter client received: " + response.message)
    response = stub.SayHelloAgain(helloworld_pb2.HelloRequest(name='you'))
    print("Greeter client received: " + response.message)


if __name__ == '__main__':
    run()
