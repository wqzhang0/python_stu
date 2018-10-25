from functools import wraps
from inspect import signature


def typeassert(*ty_args,**ty_kwargs):
    def decorate(func):
        if not __debug__:
            return func
        sig = signature(func)

        bound_types = sig.bind_partial(*ty_args,**ty_kwargs).arguments

        @wraps(func)
        def wrapper(*args,**kwargs):
            bound_values = sig.bind(*args,**kwargs)
            for name,value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value,bound_types[name]):
                        raise TypeError('Argument {} must be {}'.format(name,bound_types))
            return func(*args,**kwargs)

        return wrapper

    return decorate

@typeassert(int, int)
def add(x, y):
    return x + y

add(1,2)
# add(1,'hello')
@typeassert(int, z=int)
def spam(x, y, z=42):
    print(x, y, z)
spam(2,3)
