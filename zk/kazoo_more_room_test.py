import datetime
import random
import threading
import time

from kazoo.client import KazooClient

from zk.zk_wrapper import zkWatch

"""
自己笔记本
700  房间 400人 500count/s
50   房间 400人 220count/s
ecs 8核16G 
cpu  60% 1200count /1s 5个进程  每个进程400-600 线程
cpu  15% 500count /1s 1个进程  每个进程400-600 线程
"""

zk = KazooClient(hosts='127.0.0.1:2181')

ROOT = "/1"
zk.start()

index = 0

room_list = list(range(100, 150))
room_list = [str(x) for x in room_list]


def random_room():
    # return "11111"
    return random.choice(room_list)


old_date = datetime.datetime.now()


def test_call(_data):
    rlock.acquire()
    global count
    global old_date
    count = count + 1
    t =  Thread.currentThread()
    print(__)

    rlock.release()


def run():
    # for x in range(1):
    zkWatch(zk, "/".join([ROOT, random_room()]), test_call, "")


count = 0

rlock = threading.RLock()
for i in range(2):
    t = threading.Thread(target=run, args=(),name=i)
    t.start()
while True:
    time.sleep(1)
