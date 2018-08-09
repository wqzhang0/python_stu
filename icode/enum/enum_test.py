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