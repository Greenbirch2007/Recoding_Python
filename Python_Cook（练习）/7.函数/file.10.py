#　7.10  在回调函数中携带额外的状态

#　７．１０．１　　问题
#　我们正在编写需要使用回调函数的代码(比如，事件处理例程，完成回调等)，但是希望回调函数可以携带额外的状态以便在回调函数内部使用

#　７．１０．２　解决方案

#　本节中提到的对回调函数的应用可以在许多库和框架中找到————尤其是那些和异步处理相关的库和框架。为了说明和测试的目的，我们首先定义
#下面的函数，它会调用一个回调函数：

def apply_async(func,args,*,callback):
    #compute the result
    result = func(*args)
    # invoke the callback with the result
    callback(result)

#　在现实世界中，类似这样的代码可能会完成各种高级的处理任务，这会涉及到线程，进程和定时器等。我们这里只是把注意力集中在对回调函数的调用上


def print_result(result):
    print("Got:",result)
#
def add(x,y):
    return x+y
#
# t = apply_async(add,(2,3),callback=print_result)
# print(t)

# t1 = apply_async(add,('hello','world'),callback=print_result)
# print(t1)

# 我们会注意到函数print_result()仅接受一个单独的参数，也就是result,这里并没有传入其他的信息到函数中。有时候当我们希望回调函数
# 可以同其他变量或部分环境进行交互时，缺乏这类信息就会带来问题

# 一种在回调函数中携带额外信息的方法是使用绑定方法(bound-method)而不是普通的函数。比如，下面这个类保存了一个内部的序列号码，每当
# 接收到一个结果时就递增这个号码


class ResultHandler:
    def __init__(self):
        self.sequence = 0
    def handler(self,result):
        self.sequence += 1
        print("[{}] Got:{}".format(self.sequence,result))

# 要使用这个类，可以创建一个类实例并将绑定方法handler当做回调函数来用

r = ResultHandler()

t = apply_async(add,(2,3),callback=r.handler)
print(t)

# 作为类的替代方案，也可以使用闭包来捕获状态


def make_handler():
    sequence = 0
    def handler(result):
        nonlocal sequence
        sequence += 1
        print('[{}] Got: {}'.format(sequence,result))


handler = make_handler()
t = apply_async(add,(2,3),callback=handler)
print(t)

# 除此之外，还可以利用协程(coroutine)来完成同样的任务
# 对于协程来说，可以使用它的send()方法作为回调函数，
# 也可以通过额外的参数在回调函数中携带状态，然后用partial()来处理参数个数的问题

class SequenceNo:
    def __init__(self):
        self.sequence = 0

def handler(result,seq):
    seq.sequence += 1
    print('[{}] Got: {}'.format(seq.sequence,result))

seq = SequenceNo()

from functools import partial

t = apply_async(add,(2,3),callback=partial(handler,seq=seq))
print(t)

# 7.10.3 讨论
# 如果想让回调函数在涉及多个步骤在任务处理中能够继续执行，就必须清楚应该如何保存和还原相关的状态

# 主要有两个方法可用于捕获和携带状态。可以在类实例上携带状态(将状态附加到绑定方法上)，也可以在闭包中携带状态。
# 如果所有需要做的就是在回调函数中传入额外的值，那么最后提到的那个有关partial()的技术管用