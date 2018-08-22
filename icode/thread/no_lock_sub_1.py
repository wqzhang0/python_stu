import threading
import time
"""
https://www.cnblogs.com/lidagen/p/7237674.html
"""

def sub():
    global count

    temp = count

    print(count)

    time.sleep(2)

    count = temp + 1
    print(count)


count = 0

l = []
for i in range(100):
    t = threading.Thread(target=sub, args=())
    t.start()

    l.append(t)
for t in l:
    t.join()
print(count)
