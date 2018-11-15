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

# 在这种情况下，用户可以调用定义的静态方法，但是没法以普通的方式创建出实例。如下

Spam.grok(42)

# 现在，假设我们想实现单例模式(即，这个类只能创建唯一的一个实例。)相对来说这就很直接了 如下


class Singleton(type):
    def __init__(self,*args,**kwargs):
        self.__instance = None
        super().__init__(*args,**kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args,**kwargs)
            return self.__instance

        else:
            return self.__instance

# example
class Spam(metaclass=Singleton):
    def __init__(self):
        print('Creating Spam')

# 在这种情况下，这个类只能创建出唯一的实例。如下
a = Spam()
b = Spam()
print(a is b)


# 最后，假设我们想创建缓存实例(cached instance) 我们用一个元类来实现


import weakref


class Cached(type):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.__cache = weakref.WeakValueDictionary()

    def __call__(self, *args):
        if args in self.__cache:
            return self.__cache[args]
        else:
            obj = super().__call__(*args)
            self.__cache[args] = obj
        return obj


# example
class Spam(metaclass=Cached):
    def __init__(self,name):
        print('Creating Spam({!r})'.format(name))
        self.name = name

# 下面使用交互模式来展示这个类的行为

a = Spam('Guido')
b = Spam('Karson')
c = Spam('Guido')
print(a is b )
print(a is c )

# 9.13.3 讨论
# 通过元类来实现各种创建实例的模式常常比那些不涉及元类的解决方式要优雅。如果不用元类，那就的将类隐藏咋某种额外的工厂
# 函数之后。如，要实现单例模式，可能会用到如下技巧

class _Spam:
    def __init__(self):
        print('Creating Spam')

_spam_instance = None

def Spam():
    global _spam_instance
    if _spam_instance is not None:
        return _spam_instance
    else:
        _spam_instance = _Spam()
        return _spam_instance

# 尽管使用元类的解决方案涉及许多更加高级的概念，但最终的代码看起来会更加清晰，也没有那么多所谓的技巧

#８．２５　会有更多关于创建缓存实例，弱引用(weak reference)以及其他细节方面的信息