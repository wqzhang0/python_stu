import time
from task import add

if __name__ == '__main__':
    # print(add.delay(4, 4))
    result = add.delay(4, 4)
    no_rt = True
    while no_rt:
        if result.ready():
            print("result.ready True:" + result)
        print("result.ready False:" + result)
        time.sleep(1)
