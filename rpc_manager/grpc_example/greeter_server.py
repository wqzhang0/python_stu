from concurrent.futures import ThreadPoolExecutor

import grpc
import time


from rpc_manager.grpc_example import helloworld_pb2_grpc, helloworld_pb2


class Greeter(helloworld_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return helloworld_pb2.HelloReply(message='Hello,%s' % request.name)

    def SayHelloAgain(self, request, context):
        return helloworld_pb2.HelloReply(message='Hello again, %s!' % request.name)


def serve():
    grpc_server = grpc.server(ThreadPoolExecutor(max_workers=4))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), grpc_server)

    SERVICE_NAMES = (
        helloworld_pb2.DESCRIPTOR.services_by_name['Greeter'].full_name,
        # reflection.SERVICE_NAME,
    )
    # reflection.enable_server_reflection(SERVICE_NAMES, grpc_server)


    grpc_server.add_insecure_port('127.0.0.1:5000')
    grpc_server.start()
    _ONE_DAY_IN_SECONDS = 60 * 60 * 24
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        grpc_server.stop(0)


if __name__ == '__main__':
    serve()

# def run():
#   channel = grpc.insecure_channel('localhost:50051')
#   stub = helloworld_pb2_grpc.GreeterStub(channel)
#   response = stub.SayHello(helloworld_pb2.HelloRequest(name='you'))
#   print("Greeter client received: " + response.message)
#   response = stub.SayHelloAgain(helloworld_pb2.HelloRequest(name='you'))
#   print("Greeter client received: " + response.message)
