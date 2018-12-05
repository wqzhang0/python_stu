class A(object):
    def test(self):
        print('frome A')


class B(A):
    def test(self):
        print('frome B')


class C(A):
    def test(self):
        print('frome C')


class D(B):
    def test(self):
        print('frome D')


class E(C):
    def test(self):
        print('frome E')


class F(D, E):
    def test(self):
        print('frome F')


f1 = F()
f1.test()
print(F.__mro__)
