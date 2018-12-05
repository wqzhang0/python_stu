class Pair:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__()

    def __repr__(self) -> str:
        return ('Pair({0.x!r},{0.y!r})'.format(self))

    def __str__(self) -> str:
        return ('({0.x!s}, {0.y!s})'.format(self))


p = Pair(3, 4)

print(p)

_formats = {
    'ymd': '{d.year}-{d.month}-{d.day}',
    'mdy': '{d.month}/{d.day}-{d.year}',
    'dmy': '{d.day}/{d.month}{d.year}',
}


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)

d = Date(2018,12,5)

print(format(d))
a = d
print('The date is {:ymd}'.format(a))