import threading
import time

"""
https://www.cnblogs.com/lidagen/p/7237674.html

互斥锁 模拟死锁产生的情况
"""


def foo():
    lockA.acquire()
    print("foo lockA.acquire")
    lockB.acquire()
    print("foo lockB.acquire")

    lockA.release()
    lockB.release()


def bar():
    lockB.acquire()
    print("bar lockA.acquire")
    time.sleep(2)
    lockA.acquire()
    print("bar lockB.acquire")

    lockB.release()
    lockA.release()


def run():
    foo()
    bar()


count = 0

l = []
lockA = threading.Lock()
lockB = threading.Lock()  # 将锁内的代码串行化
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
