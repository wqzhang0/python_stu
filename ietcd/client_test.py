import etcd3
import time


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


if __name__ == '__main__':
    etcd = etcd3.client()

    #11秒过期
    _lease  = etcd.lease(2)
    print('#2秒过期')
    etcd.put('/GRPC/roomserver/123123','',_lease)

    # _lease.refresh()
    x= etcd.refresh_lease(_lease.id)
    while next(x):
        time.sleep(1)

        # print('fresh lease')


    #     pass
    #
    while(True):
        time.sleep(100)
