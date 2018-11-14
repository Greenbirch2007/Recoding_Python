# 9.13  利用元类控制实例的创建
# 9.13.1 问题
# 我们想改变实例创建的方式，以此来实现单例模式，缓存或其他类似的特性
# 9.13.2 解决方案
# 如果定义一个类，那么创建实例时就好像在调用一个函数一样，如下

class Spam:
    def __init__(self,name):
        self.name = name

a = Spam('Guido')
b = Spam('Diana')
# 如果想定制话这个步骤，则可以通过定制一个元类并以某种方式重新实现它的__call__()方法。为了说明这个过程，假设我们不想让任何人创建出实例：

class NoInstances(type):
    def __call__(self, *args, **kwargs):
        raise  TypeError("can't instantiate directly")


# example
class Spam(metaclass=NoInstances):
    @staticmethod
    def grok(x):
        print('Spam.grok')

# 在这种情况下，用户可以调用定义的静态方法，但是没法以