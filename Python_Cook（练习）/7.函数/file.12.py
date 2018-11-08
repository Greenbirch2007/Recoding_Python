# 7.12 访问定义在闭包内的变量

# ７．１２．１　问题
# 我们希望通过函数来扩展闭包，使得在闭包内层含义的变量可以被访问和修改

# ７．１２．２　解决方案

# 一般来说，在闭包内层定义的变量对于外界来说完全是隔离的。但是，可以通过编写存取函数(accessor function,即getter/setter方法)并将它们作为函数属性附加到
# 闭包上来提供对内层变量的访问支持，如下


def sample():
    n = 0
    # closure function
    def func():
        print('n=',n)
    # accessor methods for n

    def get_n():
        return n

    def set_n(value):
        nonlocal n
        n = value

    # attach as function attribute
    func.get_n = get_n
    func.set_n = set_n

    return func

f = sample()
f()
f.get_n()
t = f.set_n(10)
f()

# 7.12.3 讨论

# 这里的两个特性，首先，nonlocal声明使得编写函数来修改内层变量成为可能。其次，函数属性能够将存取函数以直接的方式附加到闭包函数上，它们工作
#起来更像实例的方法

# 扩展一些，就是让闭包模拟成类实例。我们索要做的就是将内层函数拷贝到一个实例的字典中然后将它返回，如下

import sys

class ClosureInstance:
    def __init__(self,locals=None):
        if locals is None:
            locals = sys._getframe(1).f_locals

            # update instance dictionary with callable
            self.__dict__.update((key,value) for key,value in locals.items() if callable(value))

    # redirect special methods

    def __len__(self):
        return self.__dict__['__len__']()

# example use

def Stack():
    items = []

    def push(item):
        items.append(item)

    def pop():
        return items.pop()

    def __len__():
        return len(items)

    return ClosureInstance()


s = Stack()
print(s)
print(s.push(6))
print(s.push(20))
print(s.push('hello'))
print(len(s))
print(s.pop())
print(s.pop())
print(s.pop())


# 采用闭包的版本要快8%.测试中的大部分事件都花在对实例变量的直接访问上，闭包要更快一些，这是因为不用涉及额外的self变量


#  从全局的角度考虑，为闭包增加方法可能会有更多的实际用途，比如我们想重置内部状态，刷新缓冲区，清除缓存或实现某种形式的反馈机制(feedback mechanism)