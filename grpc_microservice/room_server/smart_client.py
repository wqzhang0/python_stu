import grpc

from grpc_microservice.room_proto import room_server_pb2
from grpc_microservice.room_proto.room_server_pb2_grpc import RoomServerStubProxy

"""
1000次api调用  2196.0017681121826 ms

"""

def run():
    # header_adder_interceptor = header_manipulator_client_interceptor.server_access_interceptor('123')
    # for i in range(100):
    #
    #     with grpc.insecure_channel('127.0.0.1:50002') as channel:
    #         intercept_channel = grpc.intercept_channel(channel, header_adder_interceptor)
    #         stub = room_server_pb2_grpc.RoomServerStub(intercept_channel)
    #         stub.RandomJoinRoom(room_server_pb2.JoinRoomRequest(player_id=1112, type=3))
    #         print(i)
    #     pass

    # header_adder_interceptor = header_manipulator_client_interceptor.server_access_interceptor('123')

    # with grpc.insecure_channel('localhost:50002') as channel:
    #     for i in range(100):
    #         print(i)
    #         intercept_channel = grpc.intercept_channel(channel, header_adder_interceptor)
    #         # intercept_channel = channel
    #         stub = room_server_pb2_grpc.RoomServerStub(intercept_channel)
    #         response = stub.RandomJoinRoom(room_server_pb2.JoinRoomRequest(player_id=1112, type=3))
        # common_reply = response.common
        # code = common_reply.code
        # if code == 200:
        #     game_record_id = response.game_record_id
        #     print('成功 game_recod_id', game_record_id)
        # else:
        #     print('失败 error_msg', common_reply.error_msg)

    for i in range(1000):
        print(i)
        response = RoomServerStubProxy().RandomJoinRoom(room_server_pb2.RandomJoinRoomRequest(player_id=1112, type=3),debug=True)

        common_reply = response.common
        code = common_reply.code
        # if code == 200:
        #     game_record_id = response.game_record_id
        #     print('成功 game_recod_id', game_record_id)
        # else:
        #     print('失败 error_msg' ,common_reply.error_msg)

    # header_adder_interceptor = header_manipulator_client_interceptor.server_access_interceptor()

    # with grpc.insecure_channel('localhost:50051') as channel:
    #
    #     intercept_channel = grpc.intercept_channel(channel,header_adder_interceptor)
    #     # intercept_channel = channel
    #     a = RoomServerStubProxy().RandomJoinRoom(room_server_pb2.RandomJoinRoomRequest(player_id = 1112, type = 3))
    #
    #     stub = room_server_pb2_grpc.RoomServerStub(intercept_channel)
    #
    #
    #     response = stub.RandomJoinRoom(room_server_pb2.RandomJoinRoomRequest(player_id = 1112, type = 3))
    #     common_reply = response.common
    #     code = common_reply.code
    #     if code == 200:
    #         game_record_id = response.game_record_id
    #         print('成功 game_recod_id' ,game_record_id)
    #     else:
    #         print('失败 error_msg' ,common_reply.error_msg)



if __name__ == '__main__':
    run()