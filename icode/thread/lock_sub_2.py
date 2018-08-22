import threading
import time

"""
https://www.cnblogs.com/lidagen/p/7237674.html

互斥锁
"""


def sub():
    global count
    # 上锁，第一个线程如果申请到锁，会在执行公共数据的过程中持续阻塞后续线程
    # 即后续第二个或其他线程依次来了发现已经被上锁，只能等待第一个线程释放锁
    # 当第一个线程将锁释放，后续的线程会进行争抢
    lock.acquire()
    temp = count

    print(count)

    time.sleep(0.01)

    count = temp + 1
    print(count)
    lock.release()

    time.sleep(2)


count = 0

l = []
lock = threading.Lock()  # 将锁内的代码串行化
for i in range(100):
    t = threading.Thread(target=sub, args=())
    t.start()

    l.append(t)
for t in l:
    t.join()
print(count)
