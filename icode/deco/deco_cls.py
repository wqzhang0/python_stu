"""
装饰器带类参数
"""


class locker:
    node_path = None

    def __init__(self, path):
        print("locker.__init__() should be not called.")
        self.node_path = path

    # @staticmethod
    def acquire(self):
        print("locker.acquire() called :%s" % self.node_path)

    # @classmethod
    def release(self):
        print("locker.release() called :%s" % self.node_path)


def deco(cls):
    def _deco(func):
        def __deco():
            print("before %s called [%s]." % (func.__name__, cls))
            print(cls.node_path)

            cls.acquire()
            try:
                func()
            finally:
                cls.release()

        return __deco

    return _deco


lockerA = locker("123")

# lockerA.acquire()
@deco(lockerA)
def myfunc():
    print("myfunc() called.")


@deco(locker)
def myfunc2():
    print("myfunc() called.")


if __name__ == '__main__':
    print(myfunc())
    print(myfunc2())
