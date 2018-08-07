class Demo(object):
    def __init__(self, *args, **kwargs):
        print('init')

    def __new__(cls, *args, **kwargs):
        print('new')
        print(type(cls))
        return object.__new__(cls, *args, **kwargs)

    def __delete__(self, instance):
        print('delete')


class PositiveInteger(int):

    def __init__(self, value):
        super(PositiveInteger, self).__init__( abs(value))


if __name__ == '__main__':
    # demo = Demo()
    i = PositiveInteger(-3)
    print(i)