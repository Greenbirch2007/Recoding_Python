# ７．１１　内联回调函数

# ７．１１．１　问题
# 我们想让代码看起来更像一般的过程式步骤

# ７．１１．２　解决方案

# 我们可以通过生成器和协程将回调函数内联到一个函数中。为了说明，假设有一个函数会按照下面的方式调用回调函数


def apply_async(func,args,*,callback):
    #compute the result
    result = func(*args)
    # invoke the callback with the result
    callback(result)


# 下面的支持代码，涉及一个Async类和inlined_async装饰器

from queue import Queue
from functools import wraps


class Async:
    def __init__(self,func,args):
        self.func = func
        self.args = args


def inlined_async(func):
    @wraps(func)
    def wrapper(*args):
        f = func(*args)
        result_queue = Queue()
        result_queue.put(None)
        while True:
            result = result_queue.get()
            try:
                a = f.send(result)
                apply_async(a.func,a.args,callback=result_queue.put)
            except StopIteration:
                break
    return wrapper


def add(x,y):
    return x+y

@inlined_async
def test():
    r = yield  Async(add,(2,3))
    print(r)
    r = yield Async(add,('hello','world'))
    print(r)

    for n in range(10):
        r = yield Async(add,(n,n))
        print(r)
    print('gOOOOOOBY')


if __name__ == "__main__":
    import multiprocessing
    pool = multiprocessing.Pool()
    apply_async = pool.apply_async
    test()

# 这两段代码允许我们通过yield语句将回调函数变为内联式的。如下

# 7.11.3 讨论

# 首先，在涉及回调函数的代码中，问题的关键在于当前的计算被挂起，然后在稍后某个时刻再得到恢复。
# 本节的狠心在inlined_async()装饰器函数中。关键点就是对于生成器函数的所有yield语句装饰器都会逐条进行跟踪，一次一个。
