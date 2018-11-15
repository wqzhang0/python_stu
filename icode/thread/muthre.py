import os
import time
from multiprocessing.pool import Pool


def c_list():
    return [1, 2, 34]


CH = c_list()


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    print(CH)
    start = time.time()
    end = time.time()
    _c = 0
    while (end - start) < 20:
        _c = _c + 1
        CH.append(_c)
        print(id(CH))
        print('task task %s (%09s)   %s' % (name, os.getpid(), CH))
        time.sleep(1)
        end = time.time()


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    print(id(CH))

    p = Pool(2)
    for i in range(2):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
