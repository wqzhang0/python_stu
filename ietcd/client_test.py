import asyncio
import json
import pprint

import etcd3
# import etcd_minoter
import time


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


# async def fresh(_lease):
#     print("Hello world!")
#     # _lease.refresh()
#     yield from etcd_minoter.refresh_lease(_lease.id)
#     await asyncio.sleep(1)
#     print("Hello again!")


def testY():
    # while True:
    for z in [1]:
        print('刷新')
        yield z

if __name__ == '__main__':
    # client = etcd_minoter.Client()


    etcd = etcd3.client()
    # while True:
    #     _status = ietcd.status()
    #     print(_status)
    #     time.sleep(1)
    #11秒过期
    _lease  = etcd.lease(2)
    etcd.put('/GRPC/roomserver/123123','{}')
    etcd.put('/GRPC/roomserver/123124','{}')
    etcd.put('/GRPC/roomserver/123125','{}')
    etcd.put('/GRPC/roomserver/123126','{}')
    childrens = etcd.get_prefix('/GRPC')
    server = {}
    for value,_meta in childrens:
        _v = value.decode("utf-8")
        _path = _meta.key.decode("utf-8").replace('/GRPC', '').split('/')

        _module = _path[1]
        _server_name = _path[2]
        server['/{}/{}'.format(_module,_server_name)] = [ json.loads(_v,encoding='utf-8')]
        print('{} : {}  {}'.format(_v,_module,_server_name))


    pprint.pprint(server)





    # print('#2秒过期')
    # ietcd.put('/GRPC/roomserver/123123','',_lease)

    # _lease.refresh()
    # time.sleep(3)

    # etcd_minoter.refresh_lease(_lease.id)
    # fresh(_lease)
    # for x in range(100000):
    #     print('fresh lease')
    # testY()
    # list(testY())
    # loop = asyncio.get_event_loop()
    #
    # # tasks = [fresh(_lease) for x in range(1000)]
    # tasks = fresh(_lease)
    # return_value = loop.run_until_complete(asyncio.wait(tasks))