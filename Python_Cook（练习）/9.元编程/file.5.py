# 9.5  定义一个属性可有用户修改的装饰器
#　9.5.1 问题
#　我们想编写一个装饰器来包装函数，但是可以让用户调整装饰器的属性，这样在运行时能够控制装饰器的行为

#　９．５．２　解决方案
#　下面给出的解决方案对是对前面的扩展，引入了访问器函数(accessor function),通过使用nonlocal关键字声明变量来修改装饰器内部的属性。
#　之后把访问器函数作为函数属性附加到包装函数上
import time
from functools import wraps,partial
import logging



# Utility decorator to attach a function as an attribute of obj

def attach_wrapper(obj,func=None):
    if func is None:
        return partial(attach_wrapper,obj)
    setattr(obj,func.__name__,func)
    return func

def logged(level,name=None,message=None):
    '''Add logging to a function.Level is the logging
    level,name is the logger name,and message is the
    log message.If name and message aren't specified.
    they default to the function's module and name '''

    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args,**kwargs):
            wrapper.log.log(wrapper.level,wrapper.logmsg)
            return func(*args,**kwargs)

        #attach adjustable attribute
        wrapper.level = level
        wrapper.logmsg = logmsg
        wrapper.log = log
        # Attach setter functions
        @attach_wrapper(wrapper)
        def set_level(newlevel):
            nonlocal level
            level = newlevel

        @attach_wrapper(wrapper)
        def get_level():
            return level

        # alternative



        @attach_wrapper(wrapper)
        def set_message(newmsg):
            nonlocal logmsg
            logmsg = newmsg
        return wrapper
    return decorate


# example use

@logged(logging.DEBUG)
def add(x,y):
    return x+y

@logged(logging.CRITICAL,'example')
def spam():
    print('Spam!')

# 下面用交互会话展示了在完成上面的定义之后对各项属性的修改

import logging
logging.basicConfig(level= logging.DEBUG)
print(add(2,3))


import logging
logging.basicConfig(level=logging.DEBUG)

# print(add(6,6))
#
# # chanage the log message
#
# add.set_message('add called')
# print('..'*88)
# print(add(6,6))
#
# # change the log level
#
# add.set_level(logging.WARNING)
# print('..'*88)
# print(add(6,6))

# 9.5.3  讨论
# 本节示例的关键就在于访问器函数(即，set_message(),set_level()),它们以属性的形式附加到了包装函数上。每个访问函数允许对nonlocal变量赋值
# 来调整内部参数。这个特性。就是访问器函数可以跨越多个装饰器层进行传播(如果所有的装饰器都使用了@functools.wraps的话)。例如，
# 假设引入了一个额外的装饰器，如@timethis


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


@timethis
@logged(logging.DEBUG)
def countdown(n):
    while n > 0:
         n -= 1


# 就会发现访问器函数依然可以工作
countdown(66666)
print(88*'.')
countdown.set_level(logging.WARNING)
countdown.set_message('Counting down to zero')
print(88*'.')
countdown(66666)


# 如果把装饰器的顺序像下面这样颠倒一下，就会发现访问器还是能够以相同的方式工作

# 尽管这里没有给出，我们也可以通过添加如下额外的代码来实现用访问器函数返回内部的状态值
# 本节中一个微妙的地方在于为什么要在一开始使用访问器函数。比方说，我们可能会考虑其他的方案，安全基于对函数属性的直接访问，如下

# 这种方法只能用在最顶层的装饰器上。如果在当前顶层的装饰器上又添加一个装饰器(比如示例中的@timethis),这样就会隐藏下层的属性使得
# 它们无法被修改、而使用访问器函数可以绕过这个限制

# 同样重要的是，本节展示的解决方案可以作为类装饰器的一种替代方案



