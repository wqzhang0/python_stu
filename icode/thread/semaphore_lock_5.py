import threading

import time

sem = threading.Semaphore(5)


def foo():
    sem.acquire()
    time.sleep(2)
    print('ok')
    sem.release()


for i in range(100):
    t = threading.Thread(target=foo, args=())
    t.start()
