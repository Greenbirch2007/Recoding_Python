# 7.7 实现一个简单的装饰器
# 示例7.15定义了一个装饰器，它会在每次调用被装饰的函数时计时，然后把经过的时间，传入的参数和调用的结果打印出来

# 示例7.15  一个简单的装饰器，输出函数的运行时间

import time


def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter()
        name = func.__name__
        arg_str = ','.join(repr(arg) for arg in args)
        print('[%0.8fs]%s(%s)-> %r'%(elapsed,name,arg_str,result))
        return result
    return clocked

# 定义内部函数clocked,它接受任意个定位参数。clocked的闭包中包含自由变量func
