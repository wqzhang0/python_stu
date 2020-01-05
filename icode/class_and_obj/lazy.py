
import math
import types


class lazyproperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value

# @lazyproperty
def get_users():
    return "sdf"

class Circle:
    def __init__(self, radius,name):
        self.radius = radius
        self.name = name

    @lazyproperty
    def area(self):
        print('Computing area')
        return math.pi * self.radius ** 2

    @lazyproperty
    def perimeter(self):
        print('Computing perimeter')
        return 2 * math.pi * self.radiusv


c = Circle(4.0,'一')
# print(c.radius)
# print(c.area)
c.umame = types.MethodType(get_users, c)
# setattr(c,'uname',get_users)
# print(c.area)
print(c.uname)


