from functools import wraps


class A:
    def decorator1(self,func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            print('Decorator 1')
            return func(*args,**kwargs)
        return wrapper
    @classmethod
    def decorator2(cls,func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            print('Decorator 2')
            return func(*args,**kwargs)
        return wrapper()


a = A()
@a.decorator1
def spam():
    pass

@A.decorator2
def grok():
    pass


"""
@property
它为什么要这么定义的主要原因是各种不同的装饰器方法会在关联的 property 实例上操作它的状态。 
因此，任何时候只要你碰到需要在装饰器中记录或绑定信息，那么这不失为一种可行方法
"""
class Person:
    # first_name = property()
    @property
    def first_name(self):
        return self._first_name
    # first_name = property()

    # @first_name.getter
    # def first_name(self):
    #     return self._first_name

    @first_name.setter
    def first_name(self,value):
        if not isinstance(value,str):
            raise TypeError('Ecpeted a string')
        self._first_name  = value

a = Person()
a.first_name = '123'
# a.first_name = 123
print(a.first_name)