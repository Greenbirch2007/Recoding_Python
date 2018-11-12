# 8.10 让属性具有惰性求值的能力
# 8.１０．１　问题

# 我们想将一个只读的属性定义为property属性方法，只有在访问它时才参与计算。但是，一旦访问了该属性，我们我们
# 希望把计算出的值缓存起来，不要每次访问它时都重新计算

# 8.10.2 解决方案
# 定义一个惰性属性最有效的方式就是利用描述符类来完成，如下

class Lazyproperty:
    def __init__(self,func):
        self.func = func

    def __get__(self, instance, cls):
        if instance is None:
            return self

        else:
            value = self.func(instance)
            setattr(instance,self.func.__name__,value)
            return value


# 要使用上述代码，可以像下面在某个类中使用它：

import math

class Circle:
    def __init__(self,radius):
        self.radius = radius

    @Lazyproperty
    def area(self):
        print('Computing area')
        return math.pi * self.radius**2

    @Lazyproperty
    def perimeter(self):
        print('Computing perimeter')
        return 2* math.pi * self.radius

c = Circle(4.0)

print(c.radius)
print(c.area)
print(c.perimeter)

# 8.10.3 讨论　
# 在大部分情况下，让属性具有惰性求值能力的全部意义就在于提升程序性能。例如，除非确实需要用到这个属性，
# 当把描述符高档类的定义体中时，访问它的属性会触发__get__(),__set__(),__delete__()方法得到执行。但是如果
# 如果一个描述符只定义了__get__()方法，则它的绑定关系比一般情况下要弱化很多(much weaker bindling).特别是，
# 只有当做访问的属性不在底层的实例字典中时，__get__()方法才会得到调用

# 示例中的lazyproperty类通过让__get__()方法以property属性相同的名称来保存计算出的值。这么做会让值保存在实例字典中，可以阻止该
# property属性重复进行计算。如下

c = Circle(66)
print(88*'_')
print(vars(c))
print(c.area)

print(vars(c))
print(c.area)
del c.area
print(vars(c))
print(c.area)


# 本节讨论的即使有一个潜在的缺点，即，计算出的值在创建之后就变成可变的(mutable)

c.area = 25
print(8*'^')
print(c.area)


# 如果需要考虑可变性的问题，可以使用另一种实现，效率降低了，而且set操作必须经由属性的getter函数来处理
# 这这比直接在实例字典中查找相应的值要慢一些。

