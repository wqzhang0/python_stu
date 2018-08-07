def fn(self, name="world"):
    print('Hello %s' % name)

def fn2(self,name="world"):
    print('byby %s' % name)

Hello = type('Hello',(object,),dict(hello=fn,byby=fn2))


h = Hello()
h.hello()
h.byby()
