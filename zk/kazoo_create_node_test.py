import datetime
import random
import threading
import time
from collections import namedtuple

import select
from kazoo.client import KazooClient
from os.path import join

from icode.redis.redis_operation_test import redisOperation
from zk.zk_wrapper import zkWatch

"""
创建子节点数
1142 count/s
"""
zk = KazooClient(hosts='127.0.0.1:2181')

ROOT = "/ROOM"
zk.start()

rds = redisOperation.get_redis()
index = 0

room_list = list(range(100, 150))
room_list = [str(x) for x in room_list]


def random_room():
    return "/RC_NODE"
    # return random.choice(room_list)


if zk.exists(random_room()) is None:
    zk.create(random_room())

print(datetime.datetime.now())


def create():
    zk.create(random_room() + "/", ephemeral=True, sequence=True)
    room_incr = rds.incr(random_room())
    if room_incr % 8000 == 0:
        print(datetime.datetime.now())
    if room_incr % 200 == 0:
        for x in range(200):
            t = threading.Thread(target=create, name="")
            t.start()


for x in range(500):
    t = threading.Thread(target=create, name="")
    t.start()

while (True):
    time.sleep(1000)
