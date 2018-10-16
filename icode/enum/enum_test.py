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

@unique
class GAME_SCENES(Enum):
    """游戏场景"""
    UNREAD = "UNREAD"
    READ = "READ"
    CHOSSE_CHARACTER = "CHOSSE_CHARACTER"
    READ_CHARACTER_INFO = "READ_CHARACTER_INFO"
    SELF_INTRO = "SELF_INTRO"
    SEARCH_CLUE = "SEARCH_CLUE"
    SPEAK = "SPEAK"
    MURDER = "MURDER"
    PK_SPEAK = "PK_SPEAK"
    PUBLIC_CHAT = "PUBLIC_CHAT"
    OVER_PUBLIC_CHAT = "OVER_PUBLIC_CHAT"



if __name__ == '__main__':
    print(GAME_SCENES.PUBLIC_CHAT.value)

    print(Weekday.Sat)
    print(Weekday.Sat.value)
    print(type(Weekday.Sat))
    print(type(Weekday.Sat.value))
    print(Weekday.Fri.value)
    print(type(Weekday.Fri.value))

    print(Weekday['Sun'].value)
    print(Weekday.Sun.name)
    print(type(Weekday.Sun.name))

    print(Weekday(2))

    # Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
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