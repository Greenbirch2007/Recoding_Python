# #  16.2  用作协程的生成器的基本行为
#
#
# #  示例16-1  可能是协程最简单的使用示例
#
#
# def simple_coroutine():
#     print('-> coroutine started')
#     x = yield
#     print('-> coroutine received:',x)
#
#
# my_coro = simple_coroutine()
# print(my_coro)
# print(88*'~')
# print(next(my_coro))
# my_coro.send(66)
#
#
# # 1. 协程使用生成器函数定义:定义体中有yield关键字
# #2.　yield在表达式中使用：如果协程只需从客户那里接收数据，那么产出的值是None--这个值是隐式指定的，因为yield关键字右边没有表达式
# #　３．　　与创建生成器的方式一样，调用函数得到生成器对象
# #　４．　首先要调用next()函数，因为生成器还没有启动，　没有yield语句处暂停，所以一开始无法发送数据
# #　５．　调用这个方法后，协程定义体中的yield表达式会计算出４２；现在，协程会恢复，一直运行到下一个yield表达式，或终止
# #　６．这里，控制权流动到协程定义体的末尾，导致生成器像往常一样抛出StopIteration异常
#
#
#
# #　　协程可以身处４个状态中的一个．当前状态可以使用inspect.getgeneratorstate()函数确定，该函数会返回下述字符串中的一个
#
# #　１．　'GEN_CREATED'  等待开始执行
# #　２．　'GEN_RUNNING'  解释器正在执行
# #　３．　'GEN_SUSPENDED'  在yield表达式处暂停
# #　４．　　'GEN_CLOSED'  执行结束
#
# #　因为send方法的参数会成为暂停的yield表达式的值，所以，仅当协程处于暂停状态时才能调用send方法，例如my_coro.send(42).
# #　如果协程还没有激活(即，状态是'GEN_CREATED')，情况就不同了．因为，始终要调用next(my_coro)激活协程－－－也可以调用
# #　my_coro.send(None),效果一样
# #　如果创建协程对象后立即把None之外的值发给它，会有错误．只有在多线程应用中才能看到这个状态，此外，生成器对象在自己身上调用getgeneratorstate函数也是可以的
#
# #　最先调用next(my_coro)函数这一步通常称为"预激"(prime)协程(即，让协程向前执行到第一个yield表达式，准备好作为活跃的协程使用)
#
#
# 　示例１６－２　　产出两个值的协程

def simple_coro2(a):
    print('-> Started:a = ',a)
    b = yield a
    print('-> Received:b =',b)
    c = yield a + b
    print('-> Received:c = ',c)


my_coro2 = simple_coro2(16)
from inspect import getgeneratorstate
print(getgeneratorstate(my_coro2))

#　执行simple_coro2协程的３个阶段(注意，各个阶段都在yield表达式中结束，而且下一个阶段都从那一行代码开始，然后再把yield表达式的值赋给变量)

#　
