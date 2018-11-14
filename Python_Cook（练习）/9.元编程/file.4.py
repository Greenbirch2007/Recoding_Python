# 9.4 定义一个可接受参数的装饰器

# 9.4.1  问题
# 我们想编写一个可接受参数的装饰器函数
# 9.4.2 解决方案
# 让我们用一个例子来说明接受参数的过程。假设我们想编写一个为函数添加日志功能的装饰器，但是又允许用户指定日志的等级以及一些其他的细节作为参数。
# 下面是定义这个装饰器的可能做法

from functools import wraps
import logging



def logged(level,name=None,message=None):
    '''
    Add logging to a function,level is the logging
    level,name is the logger name,and message is the
    log message. If name and message aren't specified,
    they default to the function's module and name.
    '''

    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__


        @wraps(func)
        def wrapper(*args,**kwargs):
            log.log(level,logmsg)
            return func(*args,**kwargs)
        return wrapper
    return decorate



# examle use

@logged(logging.DEBUG)
def add(x,y):
    return x+y

@logged(logging.CRITICAL,'example')
def spam():
    print('Spam!')


print(add(6,8))
print(spam)
# 初看上去这个实现有技巧性，但是其中的思想很简单。最外层的logged()函数接受所需的参数，并让它们对装饰器的内层函数可见。
#内层的decorate()函数接受一个函数并给它加上一个包装层。关键部分在于这个包装层可以使用传递给logged()的参数

# 9.4.3  讨论
# 编写一个可接受参数的装饰器是需要一些技巧的，因为这会设计底层的调用顺序。具体来说，如果这样的代码：

@decorator(x,y,z)
def func(a,b):
    pass

#装饰的过程会按照下列方式来进行

def func(a,b):
    pass
func = decorator(x,y,z)(func)

# 请仔细观察，decorator(x,y,z)的结果必须是一个可调用对象，这个对象反过来接受一个函数作为输入，并对其进行包装


