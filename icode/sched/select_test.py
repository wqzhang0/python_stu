import select

import datetime

if __name__ == '__main__':
    print("start")
    print(datetime.datetime.now())
    a, b, c = select.select([], [], [], 1)
    print("end")
    # print(datetime.datetime.now())
    # for i in range(10000000):
    #     if i % 10000 == 0:
    #         print(datetime.datetime.now())
    # print(datetime.datetime.now())