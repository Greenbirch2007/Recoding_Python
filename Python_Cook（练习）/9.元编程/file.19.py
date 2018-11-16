# 9.19 在定义的时候初始化类成员

# 9.19.1 问题
#　我们想在定义类的时候对部分成员进行初始化，而不是在创建类实例的时候完成
# 9.19.2 解决方案
# 在定义类的时候执行初始化或配置操作是元类的经典用途。从本质上说，元类是在定义类的时候触发执行，
# 此时可以执行额外的步骤

import operator

class StructTupleMeta(type):
    def __init__(cls,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for n,name in enumerate(cls._fields):
            setattr(cls,name,property(operator.itemgetter(n)))

class StructTuple(tuple,metaclass=StructTupleMeta):
    _fields = []
    def __new__(cls, *args):
        if len(args) != len(cls._fields):
            raise  ValueError('{} arguments required.'.format(len(cls._fields)))
        return super().__new__(cls,args)

# 上述代码允许我们定义简单的基于元组的数据结构，如下


class Stock(StructTuple):
    _fields = ['name','shares','price']

class Point(StructTuple):
    _fields = ['x','y']


# 如下

s= Stock('apple',50,91.9)
print(s)
print(s[0])
print(s.name)
print(s.shares*s.price)


# 9.19.3 讨论

# 本节中，类StructTupleMeta接受类属性_fields中的属性名称，并将它们转换为属性方法，使得这些方法能够访问到元组的某个特定槽位。函数operator.itemgetter()
# 创建了一个访问器函数(accessor function),而函数property()将其转换成一个property属性


# 如何知道不同的初始化步骤在什么时候发生。StructTupleMeta中的__init__()方法针对每个定义的类只会调用一次。参数cls代表着所定义的类。从本质上说，
# 我们给出的代码利用类变量_fiels来接受新定义的类，然后为其添加一些新的部分

# 类StructTuple作为公共基类让用户从它继承。类中的__new__()方法负责产生新的实例。这里对__new__()使用有些不同寻常，部分原因在于我们修改了元组的
# 调用签名，这使得现在的调用约定看起来和不同调用一样

s = Stock('APLL',50,99.99)  # OK
s= Stock(('afa',100,100.10)) # error


# 和__init__()不同，__new__()方法会在类实例创建出来之前得到触发。由于元组是不可变对象(immutable),一旦它们被创建出来就无法做任何修改了。因此
# __init__()方法在类实例创建的过程中触发的时机太晚，以至于没法按我们想要的方式修改实例。这就是为什么要定义__new__()的原因

