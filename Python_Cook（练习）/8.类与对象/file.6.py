# 8.6  创建可管理的属性
# 8.6.1 问题
# 在对实例属性的获取和设定上，我们希望增加一个额外的处理过程(比如类型检查或验证)
# 8.6.2 解决方案
# 要自定义属性的访问，一种简单的方式是将其定义为property(即把类中定义的函数当做一种属性来使用)。比如，下面的代码定义了一个property
# 增加了对属性的类型检查


# class Person:
#     dction
#     @f first_name(self,value):
#       first_name.setter
#     de  if not isinstance(value,str):
#             raise TypeError('Expected a string')
#         self._first_name = value
# ef __init__(self,first_name):
#         self.first_name = first_name
#
#     # getter function
#     @property
#     def first_name(self):
#         return self._first_name
#
#     # setter fun
#     # deleter function (option1)
#     @first_name.deleter
#     def first_name(self):
        # raise AttributeError("can't delete attribute")


# 一共三个互相关联的方法，它们必须有着相同的名称。第一个方法是一个getter函数，并且将first_name定义为了property属性。其他两个方法将可选的
# setter和deleter函数附加到了first_name属性上。除非first_name已经通过@property的方式定义为了property属性，否则是不能定义@first_name.setter
# @first_name.deleter 装饰器的



# property的重要特性就是它看起来就像一个普通的属性，但是根据访问它的不同方式，会自动触发getter,setter,deleter方法，如下

#
# a = Person('Karson')
# t = a.first_name
# print(t)
# a.first_name = 42
# del a.first_name


# 当我们实现一个property时，底层的数据仍然需要被保存到某个地方。因此在get和set方法中，可以我们是直接对_first_name进行操作的，这就是数据实际保存的地方
#　此外，为什么在__init__()方法中设定的是self.first_name而不是self._first_name呢？在这个例子中，property的全部意义在于我们设置属性时可以执行类型检查、
#　因此，很有可能你想让这种类型检查在初始化的时候也可以进行。因此，在__init__()中设置self.first_name,实际上会调用到setter方法(因此就会跳过
# self.first_name而去访问self._first_name )

class Person:
    def __init__(self,first_name):
        self.set_first_name(first_name)

    # getter function

    def get_first_name(self):
        return self._first_name

    # setter function
    def set_first_name(self,value):
        if not isinstance(value,str):
            raise TypeError("Expected a string")
        self._first_name = value

    # delete function(optional)
    def del_first_name(self):
        raise AttributeError("can't delete attribute")

    # make a property from existing get/set methods
    name = property(get_first_name,set_first_name,del_first_name)

# 8.6.3  讨论
# property属性实际上就是把一系列的方法绑定到一起。如果检查类的property属性，就会发现property自身所持有的属性fget,fset,fdel所代表的原始方法，如下

# print(Person.del_first_name.fget)
# 一般来说我们不会直接取调用fget或fset,但是当我们访问property属性时会自动触发对这些方法的调用
#只有当确实需要在访问属性时完成一些额外的处理任务时，才应该使用property.

# property也可以用来定义需要计算的属性。这类属性并不会实际保存起来，而是根据需要要完成计算，如下

import math

class Circle:
    def __init__(self,radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius**2

    @property
    def perimeter(self):
        return 2*math.pi * self.radius

# 这里对property的使用使得实例的接口变得非常统一，radius,area以及perimeter都能够简单地以属性的形式进行访问，而不必将属性和方法调用混在一起使用，如下

c = Circle(4.0)

print(c.radius)
print(c.area)
print(c.perimeter)


# 尽管property带来了优雅的编程接口，但有时候我们还是希望能够直接使用getter和setter函数，如下

p = Person('Karson')
print(p.get_first_name())
print(p.set_first_name('larry'))
print(p.get_first_name())

# 这种情况常常会出现在当Python代码需要被集成到一个更为庞大的系统基础设施或程序的时候。比方说，也许有一个Python类需要根据远程
# 过程调用(RPC)或分布式对象插入到一个大型的分布式系统中。在这种情况下，直接显式地采用get/set方法(作为普通的方法调用)
# 要比通过property来隐式调用这类函数更加方便和简单
#　不重复编写property，利用描述符或闭包能够更好地完成同样都任务