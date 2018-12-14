# 16.7  使用 yield from


# 1. yield from 可用于简化for循环中的yield表达式


def gen():
    for c in 'ABC':
        yield c
    for i in range(1,4):
        yield i

print(list(gen()))

# 可以改写如下

def gen1():
    yield from 'ABCD'
    yield from range(1,9)

print(list(gen1()))


#  示例１６－１６　　使用yield from 链接可迭代的对

def chain(*iterables):
    for it in iterables:
        yield from it

s = 'ABC'
t = tuple(range(3))
print(list(chain(s,t)))

# itertools 模块提供了优化版chain函数，使用c语言编写
#  yield　from x　表达式对ｘ对象所做的第一件事是，调用iter(x),从中获取迭代器．因此x可以是任何可迭代的对象

#  可是，如果yield from 结构唯一的作用四替代产出值的嵌套for循环，这个结构很有可能不会添加到python语言中．yield from 结构的本质作用无法
#  通过简单的可迭代对象说明，而要发散思维，使用嵌套的生成器．因此，引入yield from 结构的把职责委托给子生成器的句法


#  yield from 的主要功能是打开双向通道，把最外层的调用方与最内层的子生成器连接起来，这样二者可以直接发送和产出值，还可以直接传入异常，而不用在位于
#  中间的协程中添加大量处理异常的样板代码．有了这个结构，协程可以通过以前不可能的方式委托职责

#  若想使用yield from 结构，就要大幅改动代码．有以下专门的术语


#  １．　委派生成器　　 包含yield from <iterable>表达式的生成器函数

#  ２．　子生成器　　从yield from 表达式中<iterable>部分获取的生成器

#  ３．　　调用方　　是指调用委派生成器的客户端代码

#  注意，子生成器可能是简单的迭代器，只实现了__next__方法，但是,yield from 也能处理这种子生成器．引入yield from 结构的目的是为了支持实现了
#  ＿_next__,send,close和throw方法的生成器

#  委派生成器在yield from 表达式处暂停时，调用方可以直接把数据发给子生成器，子生成器再把产出的值发给调用方．子生成器返回之后，解释器会抛出StopIteration异常，
#  并把返回值加到异常对象上，此时委派生成器会恢复

#  任何yield from 链条都必须由客户驱动，在最外层委派生成器上调用next()函数或.send()方法，可以隐式调用，例如for循环