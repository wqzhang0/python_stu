# 使用位置参数
print('my name is {} ,age {}'.format('hoho', 18))
print('my name is {1} ,age {0}'.format(10, 'hoho'))
print('my name is {1} ,age {0} {1}'.format(10, 'hoho'))

li = ['hili', 18]
print('my name is {} ,age {}'.format(*li))

# my name is hoho ,age 18
# my name is hoho ,age 10
# my name is hoho ,age 10 hoho
# my name is hili ,age 18

# 使用关键字参数
# 关键字参数值要对得上，可用字典当关键字参数传入值，字典前加**即可
hash = {'name':'hoho','age':18}
print('my name is {name},age is {age}'.format(name='hoho', age=19))
'my name is hoho,age is 19'
print('my name is {name},age is {age}'.format(**hash))
# 'my name is hoho,age is 18'


# 填充与格式化

print('{0:*>10}'.format(10))
# '********10'
print('{0:*<10}'.format(10))
# '10********'
print('{0:*^10}'.format(10))
# '****10****'