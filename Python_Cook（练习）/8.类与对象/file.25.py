# 8.25 创建缓存实例
# 8.25.1 问题

# 当创建类实例时我们想返回一个缓存引用，让其指向上一个用同样参数(如果有的话)创建出的类实例

# 8.25.2 解决方案
# 这个文常常出现在我们想确保针对某一组输入参数只会有一个类实例存在时。现实中的例子包括一些库的行为。比如在logging模块中，
# 给定一个名称只会关联到一个单独的logger实例


import logging

a = logging.getLogger('foo')
b = logging.getLogger('bar')

print(a is b)
c = logging.getLogger('foo')
print(a is c)

#
# # 要实现这一行为，应该使用一个与类本身相分离的工厂函数。如下
#
# class Spam:
#     def __init__(self,name):
#         self.name = name
#
# import weakref
# _spam_cache = weakref.WeakValueDictionary()
#
# def get_spam(name):
#     if name not in _spam_cache:
#         s = Spam(name)
#         _spam_cache[name]= s
#     else:
#         s = _spam_cache[name]
#     return s
#
# a = get_spam('foo')
# b = get_spam('bar')
# print(a is b)

# 8.25.3 讨论
# 要想修改实例创建的规则，编写一个特殊的工厂函数常常是一个简单的方法。此时，一个常被提到的问题就是是否可以有个好的方法？
# 例如，我们可以考虑定义类的__new__()方法


import weakref

class Spam:
    _spam_cache = weakref.WeakValueDictionary()
    def __new__(cls, name):
        if name in cls._spam_cache:
            return cls._spam_cache[name]
        else:
            self = super().__new__(cls)
            cls._spam_cache[name] = self
            return self

    def __init__(self,name):
        print('Initializing Spam')
        self.name = name

# 要想解决实例缓存后会重复初始化的问题，需要采用另一种方法

# 本节中对弱引用的运用与垃圾收集有着极为重要的关系。当维护实例缓存时，只要在程序中实际用到了它们，那么通常希望将对象保存在
#　缓存中。WeakValueDictionary会保存这那些被引用的对象，只要它们存在于程序中的某处即可。否则，当实例不再被使用时，字典的键就会小时



# 通过使用元类，缓存机制以及其他的创建模式(creational pattern)通常能够以更加优雅的方式解决问题i