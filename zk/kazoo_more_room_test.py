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
700  房间 400人 500count/s
50   房间 400人 220count/s
"""
zk = KazooClient(hosts='127.0.0.1:2181')

ROOT = "/ROOM"
zk.start()

rds = redisOperation.get_redis()
index = 0

room_list = list(range(100, 150))
room_list = [str(x) for x in room_list]


def random_room():
    # return "111"
    return random.choice(room_list)


def test_call(_data):
    room_incr = rds.incr("ROOM_100")
    if room_incr % 8000 == 0:
        print(datetime.datetime.now())
    if room_incr % 200 == 0:
        for x in range(200):
            # self, zk, biz_path, callback
            t = threading.Thread(target=zkWatch, args=(zk, "/".join([ROOT, random_room()]), test_call, "wolegecao"),
                                 name="")
            t.start()


print(datetime.datetime.now())

for x in range(500):
    t = threading.Thread(target=zkWatch, args=(zk, "/".join([ROOT, random_room()]), test_call, "wolegecao"),
                         name="")
    t.start()
while (True):
    time.sleep(1000)
