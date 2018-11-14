# 9.2 编写装饰器时如何保存函数的元数据


# 9.2.1 问题
# 我们已经编写好了一个装饰器，但是当将它用在一个函数上时，一些重要的元数据比如函数名，文档字符串，函数注解以及调用签名都丢失了

# 9.2.2  解决方案
# 每当定义一个装饰器时，应该总是记得为底层的包装函数添加functools库中的@wraps装饰器   如下


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

# 下面使用这个装饰器的示例，并且展示了如何检视结果函数的元数据


@timethis
def countdown(n:int):
    '''Counts down'''
    while n > 0:
        n -= 1


# countdown(888888)
# print(countdown.__name__)
# print(countdown.__doc__)
# print(countdown.__annotations__)

# 9.2.3  讨论
# 编写装饰器的一个重要部分就是拷贝装饰器的元数据。如果忘记使用@wraps,就会发现被包装的函数丢失了所有有用的信息，例如，如果忽略@wraps,
# @wraps装饰器的一个重要特性就是它可以通过__wrapped__属性来访问被包装的那个函数。例如，如果希望直接访问被包装的函数，如下

# print(countdown.__wrapped__(111))


# __wrapped__属性的存在同样使得装饰器函数可以合适地将底层被包装函数的签名暴露出来，如下
from inspect import signature
print(signature(countdown))
# 常会提到的一个问题是如何让装饰器直接拷贝被包装的原始函数的调用签名(即，不使用*args,**kwargs).一般来说，如果不采用涉及生成代码字符串
#　和exec()的技巧，那么这很难实现。通常我们最好还是使用@wraps。这样可以依赖一个事实，底层的函数签名可以通过__wrapped__属性来传递
