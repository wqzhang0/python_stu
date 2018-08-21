import threading
import time

"""
https://www.cnblogs.com/lidagen/p/7237674.html
递归锁
RLock本身有一个计数器，如果碰到acquire，那么计数器+1
如果计数器大于0，那么其他线程无法查收，如果碰到release，计数器-1
"""


def foo():
    rlock.acquire()
    print("foo lockA.acquire")
    rlock.acquire()
    print("foo lockB.acquire")

    rlock.release()
    rlock.release()


def bar():
    rlock.acquire()
    print("bar lockA.acquire")
    time.sleep(2)
    rlock.acquire()
    print("bar lockB.acquire")

    rlock.release()
    rlock.release()


def run():
    foo()
    bar()


count = 0

l = []
rlock = threading.RLock()
for i in range(100):
    t = threading.Thread(target=run, args=())
    t.start()

    l.append(t)
for t in l:
    t.join()
print(count)
# 输出结果：只有四行，因为产生了死锁阻断了
# foo lockA.acquire
# foo lockB.acquire
# bar lockA.acquire
# foo lockA.acquire
