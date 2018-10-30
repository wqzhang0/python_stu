import asyncio

import etcd3
# import etcd_server
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
#     yield from etcd_server.refresh_lease(_lease.id)
#     await asyncio.sleep(1)
#     print("Hello again!")


def testY():
    # while True:
    for z in [1]:
        print('刷新')
        yield z

if __name__ == '__main__':
    # client = etcd_server.Client()


    etcd = etcd3.client()
    # while True:
    #     _status = ietcd.status()
    #     print(_status)
    #     time.sleep(1)
    #11秒过期
    _lease  = etcd.lease(2)


    # print('#2秒过期')
    # ietcd.put('/GRPC/roomserver/123123','',_lease)

    _lease.refresh()
    time.sleep(3)

    print(_lease.remaining_ttl)
    # etcd_server.refresh_lease(_lease.id)
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