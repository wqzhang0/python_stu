from enum import Enum, unique


# @unique装饰器可以帮助我们检查保证没有重复值。
@unique
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = '5'
    Fri_int = 5
    Sat = 6



if __name__ == '__main__':
    print(Weekday.Sat.value)
    print(type(Weekday.Sat))
    print(type(Weekday.Sat.value))
    print(Weekday.Fri.value)
    print(type(Weekday.Fri.value))

    print(Weekday['Sun'].value)

    print(Weekday(2))

    Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
    # Month = Enum('x', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
    # 上面这段代码等价于：
    #
    # class x(Enum): Jan = 1
    #
    #
    # Feb = 2
    # Mar = 3
    # Apr = 4
    # May = 5
    # Jun = 6
    # Jul = 7
    # Aug = 8
    # Sep = 9
    # Oct = 10
    # Nov = 11
    # Dec = 12
    # Month = x
    print(Month.Feb)
    print(Month.Feb.value)

    Weekday2 = Enum('x',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
    print(Weekday2.Jan)