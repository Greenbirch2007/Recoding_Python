#　9.6  定义一个能接手可选参数的装饰器

#  9.6.1 问题
#  我们想编写一个单独的装饰器，使其既可以想@decorator z这样不带参数使用，也可以像@decorator(x,y,z)这样可以接收可选参数。但是
#  由于简单的装饰器和可接收参数的装饰器之间存在不同的调用约定(calling convention),这样看来似乎并没有直接的方法来处理

#  9.6.2 解决方案
#  本节对于记录日志的代码做了修改，定义了一个可接受可选参数的装饰器：


from functools import wraps,partial

import logging

def logged(func=None,*,level=logging.DEBUG,name=None,message=None):
    if func is None:
        return partial(logged,level=level,name=name,message=message)

    logname = name if name else func.__module__
    log = logging.getLogger(logname)
    logmsg = message if message else func.__name__
    @wraps(func)
    def wrapper(*args,**kwargs):
        log.log(level,logmsg)
        return func(*args,**kwargs)
    return wrapper

# example use

@logged
def add(x,y):
    return x+y

@logged(level=logging.CRITICAL,name='example')
def spam():
    print('Spam!')

# 从示例中可以看到，现在这个装饰器既能以简单的形式(@logged)使用，也可以提供可以选的参数给它(即@logged(level=logging.CRITICAL,name='example'))


# 9.6.3 讨论
# 本节提到的实际上是一种编程一致性(programming consistency)的问题。当使用装饰器时，大部分程序员习惯于完全不使用任何参数，或就像示例中那样使用。
# 从技术上说，如果装饰器的所有参数都是可选的，那么可以像这样来使用：


@logged()
def add(x,y):
    return x+y

# 但是这和我们常见的形式不太一样，如果程序员忘记加上那个额外的圆括号就可能会导致常见的使用错误。本节调到的技术可以让装饰器以一致的方式使用
# 即可以带括号也可以不带括号

# 要题解代码是任何工作的，就需要对装饰器是如何施加到函数上，以及对它们的调用约定有着透彻的理解才行。以一个简单额装饰器为例


# example use

@logged
def add(x,y):
    return x+y
# 调用顺序是这样

def add(x,y):
    return x+y
add = logged(add)

# 在这种情况下，被包装的函数只是作为第一个参数简单地传递给logged.因而，在解决方案中，logged()的第一个参数就是要被包装的那个函数。
# 其他所有的参数都必须有一个默认值
# 对于一个可接受参数的装饰器，例如

@logged(level=logging.CRITICAL,name='example')
def spam():
    print('Spam!')
#  其调用顺序是这样的

def spam():
    print('spam!')
spam = logged(level=logging.CRITICAL,name='example')(spam)

# 在初次调用logged()时，被包装的函数并没有传递给logged.因此在装饰器中，被包装的函数必须作为可选参数。这样一来，反过来迫使其他的参数
#  都要通过关键字来指定。此外，当传递了参数后装饰器应该返回一个新函数，要包装的函数就作为参数传递给这个新函数。要做到这一点，我们在解决方案中利用
#  functools.partial来实现。具体，它只是返回一个部分完成的版本，除了要被包装的函数之外，其他所有的参数都已经确定好了。
