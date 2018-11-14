# 第9章元编程 。

# 软件开发中重要的一个原则：不要重复自己的工作(Don't repeat yourself.)任何时候当需要创建高度重复的代码是，通常需要寻找一个更加有效的
# 解决方案。在Python中，这类问题常被归类为"元编程"。元编程的主要目标是创建函数和类，并用它们来操纵代码(比如说修改，生成或包装已有的代码)
# Python中基于这个目的的主要特性包括装饰器，类装饰器及元类。
# 但是还会有其他的主题，包括对象签名，用exec()来执行代码以及检查函数和类的内部结构。
# 本章主要目的是探讨各种欧冠呢元编程技术，通过示例来讲解如何利用这些技术来自定义Python的行为，使其能够满足我们不同寻常的需求

# 9.1  给函数添加一个包装
# 9.1.1  问题

#  我们想给函数加上一个包装层(wrapper layer) 以及添加额外的处理(如，记录日志，计时统计)

# 9.1.2 解决方案
# 如果需要用额外的代码对函数做包装，可以定义一个装饰器函数。如下


import time

from functools import wraps


def timethis(func):
    '''Decorator that reports the execution time.'''

    @wraps(func)
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(func.__name__,end-start)
        return result
    return wrapper


# 下面使用这个装饰器的实例


@timethis
def countdown(n):
    '''Counts down'''
    while n > 0:
        n -= 1


countdown(999999)


# 9.1.3 讨论
# 装饰器就是一个函数，它可以接收一个函数作为输入并返回一个新的函数作为输出
# 内建的装饰器比如@staticmethod,@classmethod,@property的工作方式也是一样

class A:
    @classmethod
    def method(cls):
        pass

class B:
    # Equivalent definition of a class method
    def method(cls):
        pass
method =classmethod(method)


# 装饰器内部的代码一般会涉及创建一个新的函数，利用*args,**kwargs来接受任意的参数。在这个函数内部，我们需要调用原来的输入参数
# （即被包装的那个函数，它就是装饰器的输入参数） 并返回它的结果。但是，也可以添加任何想要添加的额外代码(例如计时处理)。这个新创建
# 的wrapper函数会作为装饰器的结果返回，取代了原来的函数
# 注意，装饰器一般来说不会修改调用签名，也不会修改被包装函数返回的结果。这里对*args,**kwargs的使用是为了确保可以接收任何形式的输入参数。
# 装饰器的返回值几乎总是调用func(*args,**kwargs)的结果一直，这里的func就是那个未被包装过的原始函数
# 在生产环境中，编写装饰器，咬住以，比如示例中对装饰器@wraps(func)的使用就是一个容易忘记的技术，它可以用来保存函数的元数据。
