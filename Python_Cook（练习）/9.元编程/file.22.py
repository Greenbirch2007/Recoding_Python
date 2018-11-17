# 9.22  以简单的方式定义上下文管理器

# ９．２２．１ 问题　
# 我们想实现新形式的上下文管理器，然后在with 语句中使用
# 9.22.2 解决方案
# 编写一个新的上下文管理器，其中最直接的一个防护四就是使用contextlib模块中的@contextmanager装饰器。如下，我们用上下文管理器来计时代码块的执行时间



import time
from contextlib import contextmanager


@contextmanager
def timethis(label):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print('{}:{}'.format(label,end-start))

# examle

with timethis('counting'):
    n = 1000000
    while n > 0:
        n -= 1

# 在timethis()函数中，所有位于yield之前的代码会作为上下文管理器的__enter__()方法来执行。而所有位于yield之后的diam会作为__exit__()方法
# 执行。如果产生异常，则会在yield语句中抛出

# 下面是一个更加高级的上下文管理器，其中实现了对列表对象的处理


@contextmanager
def list_transaction(orig_list):
    working = list(orig_list)  # enter
    yield working     # exit
    orig_list[:]= working

# 这采用的思路是只有当整个代码块执行结束且没有产生任何异常时，此时对列表做出的修改才会真正生效

items = [1,2,3]
with list_transaction(items) as  workging:
    workging.append(6)


print(items)

# 9.22.3  讨论
# 一般来说，要编写一个上下文管理器，需要定义一个带有__enter__()和__ext__()方法的类，如下


import time

class timethis:
    def __init__(self,label):
        self.label = label
    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.time()
        print('{}:{}'.format(self.label,end-self.start))


# @contextmanager只适用于编写自给自足型(self-contained)的上下文管理器函数。如果有一些对象(比如，文件，网络连接或锁)需要支持在with语句中使用。
# 那么还是要分别实现__enter__()和__exit__()方法啊