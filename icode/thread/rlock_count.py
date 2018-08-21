import threading

"""
用递归锁计数
"""


def run():
    while True:
        rlock.acquire()
        global count
        count = count + 1
        if count % 80000 == 0:
            print(count)
        rlock.release()
count = 0

l = []
rlock = threading.RLock()
for i in range(800):
    t = threading.Thread(target=run, args=())
    t.start()
    l.append(t)
for t in l:
    t.join()
