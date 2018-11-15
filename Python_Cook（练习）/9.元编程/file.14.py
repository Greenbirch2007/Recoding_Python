# 9.14  获取类属性的定义顺序
#  9.14.1 问题
#  我们想自动记录下属性和方法在类中定义的顺序，这样就能利用这个顺序来完成各种操作(例如序列化处理，将属性映射到数据库中等)

#  9.14.2 解决方案
#  要获取类定义体中的有关信息，可以通过元类来轻松实现。在下面的示例中，元类使用OrderedDict(有序字典)来获取描述符的定义顺序

from collections import OrderedDict

# A set of descriptors for various types

class Typed:
    _expected_type = type(None)
    def __init__(self,name=None):
        self.name = name

    def __set__(self,instance,value):
        if not isinstance(value,self._expected_type):
            raise TypeError('Expected' + str(self._expected_type))
        instance.__dict__[self.name] = value

class Integer(Typed):
    _expected_type = int

class Float(Typed):
    _expected_type = float

class String(Typed):
    _expected_type = str

# metaclass that uses an OrderedDict for class body
    class OrderedMeta(type):
        def __new__(cls,clsname,bases,clsdict):
            d = dict(clsdict)
            order = []
            for name,value in clsdict.items():
                if isinstance(value,Typed):
                    value._name = name
                    order.append(name)
                d['_order']= order
                return type.__new__(cls,clsname,bases,d)


        @classmethod
        def __prepare__(cls,clsname,bases):
            return OrderedDict()

# 在这个元类中，描述符的定义顺序是通过使用OrderedDict在执行类的定义体时获取到的。得到的结果会从字典中提取出来然后保存到类的属性_order中。
# 这之后，类方法能够以各种方式使用属性_order.例如，下面这个简单的类利用这个顺序实现了一个方法，用来将实例数据序列化为一行csv数据



class Structure(metaclass=OrderedMeta):
    def as_csv(self):
        return ','.join(str(getattr(self,name)) for name in self._order)

# example use

class Stock(Structure):
    name = String()
    shares = Integer()
    price = Float()
    def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price

# 下面用交互的方式来展示Stock类

s = Stock('GOOG',100,490.1)
print(s.name)
s.as_csv()

# 9.14.3 讨论
# 本节的全部核心就在__prepare__()方法上，该特殊方法定义在元类OrderedMeta中。该方法会在类定义一开始立刻得到调用，调用时以类名和基类名称
# 作为参数。它必须返回一个映射型对象(mapping object)供处理类定义体时使用。由于返回的是OrderedDict实例而不是普通的字典，因此
# 类中各个属性间的顺序就可以方便地得到维护
#如果想使用自定义的字典型对象，那么对上述功能进行扩展也有可能，例如，可以拒绝类中出现重复的定义


# 本节最后一个需要考虑的重要部分是在元类的__new__()方法中对自定义的字典应该如何处理。尽管我们在类定义中使用的是其他形式的字典，当创建最终的类对象时，还是
# 需要将这个字典转换为一个合适的dict实例才行。这正是d = dict(clsdict)这行代码的目的所在

# 能够获取到类属性的定义顺序看起来是微不足道的，但是对于某些特定类型的应用来说确实重要的。比如，一个对象关系映射器(ORM)中，类的编写可能与示例很类似
# 而在底层，可能想获取到属性定义的顺序，以此将对象映射到数据库表项中的元组或行上(即，和示例中as_csv()方法实现的功能类似)。本节给出的解决方案
# 是直接了当的，而且通常情况下比其他方法更加简单(一般会通过在描述符类中维护一个隐藏的计数器来实现)

