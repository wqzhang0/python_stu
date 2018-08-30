import datetime
import random
import threading
import time

from kazoo.client import KazooClient

# from icode.redis.redis_operation_test import redisOperation
from kazoo.security import Permissions, OPEN_ACL_UNSAFE

"""
创建子节点数
自己笔记本 i7 1142 count/s
ecs 8核 21 个进程 cpu 60%
8w/s
"""
zk = KazooClient(hosts='127.0.0.1:2181')

ROOT = "/ROOM"
zk.start()

index = 0

room_list = list(range(100, 2050))
room_list = [str(x) for x in room_list]


def random_room():
    # return "/RC_NODE"
    return random.choice(room_list)


if zk.exists(random_room()) is None:
    zk.create(random_room())

print(datetime.datetime.now())
count = 0
_old = datetime.datetime.now()
while (True):
    print(OPEN_ACL_UNSAFE)
    zk.create(random_room() + "/", acl=OPEN_ACL_UNSAFE, ephemeral=True, sequence=True, makepath=True)
    count = count + 1
    if count % 8000 == 0:
        now = datetime.datetime.now()
        print((now - _old).total_seconds())
        _old = now
