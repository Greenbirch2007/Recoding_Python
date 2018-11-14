# 9.8 在类中定义装饰器
#  9.8.1 问题
#  我们想在类中定义一个装饰器，并将其作用域其他的函数或方法上

#  ９．８．２　解决方案
#  在类中定义一个装饰器是很直接的，但是首先我们需要理清装饰器将以什么方式来应用。具体来说，就是以实例方法还是以类方法的形式应用。

from functools import wraps


class A:
    # Decorator as an instance method
    def decorator1(self,func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            print('Decorator~~1~~')
            return func(*args,**kwargs)
        return wrapper

    # Decorator as a class method
    @classmethod
    def decorator2(cls,func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            print('Decorator~~2~~')
            return func(*args,**kwargs)
        return wrapper

# 下面的示例展示了这两种装饰器会如何应用

#  as an instance method

a = A()

@a.decorator1
def spam():
    pass

# as a class method
@A.decorator2
def grok():
    pass

# 如果观察得够仔细，就会发现其中一个装饰器来自于实例ａ,而另一个装饰器来自于类Ａ

#  9.8.3 讨论
#  在类中定义装饰器在标准库中和普遍，特别是，内建的装饰器@property实际上是一个拥有getter(),setter(),deleter()方法的类
#  每个方法都可以作为一个装饰器

class  Person:
    # create a property instance
    first_name = property()

    #apply decorator methods

    @first_name.getter
    def first_name(self):
        return self.first_name

    @first_name.setter
    def first_name(self,value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name =value


#  至于为什么要定义成这种形式，关键原因在于这的多个装饰器方法都在操纵property实例的状态。因此，如果需要装饰器在背后记录或合并信息，

#  当编写类中的装饰器时，一个常见的困惑就是如何在装饰器代码中恰当地使用self或cls参数。尽管最外层的装饰器函数比如decorator1()或decorator2()
#  需要提供一个self或cls参数(因为它们是类的一部分)，但内层定义的包装函数一般不需要包含额外的参数。这就是为什么示例中
#  两个装饰器创建的wrapper()函数并没有包含self参数的原因。唯一一种可能会用到这个参数的场景就是需要在包装函数中访问实例的某个部分。
#  鹅肉则就不必为此操心
#  关于把装饰器定义在类的内部，还有最后一一个微妙的考虑。那就是它们在继承中的潜在用途。例如，假设想把定义在类A中的装饰器施加于定义在
#  子类B中的方法上。要做到这点，需要像这样编写代码

class B(A):
    @A.decorator2
    def bar(self):
        pass

# 特别是，这里的装饰器必须定义为类方法，而且使用时必须显式地给出父类A的名称。不能使用像＠B.decorator2这样的名称，因为在
#  定义该方法的时候类B就没有创建出来