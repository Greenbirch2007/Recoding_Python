# 9.10 把装饰器作用到类和静态方法上
# 9.10.1 问题
# 我们想在类或静态方法上应用装饰器
# 9.10.2 解决方案
# 将装饰器作用到类和静态方法是简单而直接的，但是要保证装饰器在应用的时候需要放在@classmethod，@staticmethod之前，如下

import time
from functools import wraps

# a simple decorator

def timethis(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        start = time.time()
        r = func(*args,**kwargs)
        end = time.time()
        print(end-start)
        return r
    return wrapper

# class illustrating application of the decorator to different kinds of methods

class Spam:
    @timethis
    def instance_method(self,n):
        print(self,n)
        while n > 0:
            n -= 1


    @classmethod
    @timethis
    def calss_method(cls,n):
        print(cls,n)
        while n > 0 :
            n -= 1

    @staticmethod
    @timethis
    def static_method(n):
        print(n)
        while n > 0:
            n -= 1


# 上面代码中的类和静态方法应该能够正常工作，此外还为它们添加了额外的计时功能

s = Spam()
s.instance_method(66)
Spam.calss_method(66)
Spam.static_method(66)

# 9.10.3 讨论
#　如果装饰器的顺序搞错了，那么将得到错误提示。因为@classmethod和＠staticmethod并不会实际创建可直接调用的对象。相反
# 它们创建的是特殊的描述符对象.如果，尝试在另一个装饰器中向函数那样使用它们，装饰器就会崩溃。确保这些装饰器出现在@classmethod和@staticmethod之前就能解决这个问题

#　本节提到的技术有一个重要的应用场景，那就是在抽象基类中定义类方法和静态方法。例如，如果想定义一个抽象类方法，可以使用如下

from abc import  ABCMeta,abstractmethod

class A(metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    def method(cls):
        pass

# 注意两个装饰器的位置，＠classmethod必须在外层，否则代码会崩溃