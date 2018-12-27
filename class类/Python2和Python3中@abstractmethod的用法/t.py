# Python2和Python3中@abstractmethod的用法
# 抽象方法:
#  抽象方法表示基类的一个方法,没有实现,所以基类不能实例化,子类实现了该抽象方法才能被实例化
#  Python的abc提供了@abstractmethod装饰器实现抽象方法，下面以Python3的abc模块举例。


from abc import ABC,abstractclassmethod

# 如下,基类Foo的方法被@abstractmethod装饰了,所以Foo不能被实例化;
# 子类SubA没有实现基类的fun方法也不能被实例化
# 子类SubB实现了基类的抽象方法fun,所以可以实例化
class Foo(ABC):
    @abstractclassmethod
    def fun(self):
        '''please Implements in subclass'''

class SubA(Foo):
    pass

class SubB(Foo):
    def fun(self):
        print('fun in SubB')
c = SubB()
c.fun()

# 在python3.4中,声明抽象基类最简单的方式是子类化abc.ABC;
# python3.0到python3.3,必须在class语句中使用metaclass=ABCMeta
# python2 中,要使用__metaclass__=ABCMeta