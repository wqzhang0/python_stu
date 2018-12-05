class Base:
    def __init__(self):
        print('Base.__init__')


class A(Base):
    def __init__(self):
        super().__init__()
        print('A.__init__')


class B(Base):
    def __init__(self):
        super().__init__()
        print('B.__init__')


class C(Base):
    def __init__(self):
        super().__init__()
        print('C.__init__')

class D(Base):
    def __init__(self):
        super().__init__()
        print('D.__init__')

class E(Base):
    def __init__(self):
        super().__init__()
        print('D.__init__')

class X(Base):
    def __init__(self):
        super().__init__()
        print('D.__init__')

class F(A,B):
    def __init__(self):
        super().__init__()
        print('D.__init__')


class G(C,D):
    def __init__(self):
        super().__init__()
        print('D.__init__')

class H(F,G):
    def __init__(self):
        super().__init__()
        print('D.__init__')


# 为了实现继承，Python会在MRO列表上从左到右开始查找基类，直到找到第一个匹配这个属性的类为止。
#
# 而这个MRO列表的构造是通过一个C3线性化算法来实现的。 我们不去深究这个算法的数学原理，它实际上就是合并所有父类的MRO列表并遵循如下三条准则：
#
# 子类会先于父类被检查
# 多个父类会根据它们在列表中的顺序被检查
# 如果对下一个类存在两个合法的选择，选择第一个父类
print(C.mro())
print(F.mro())
print(H.mro())