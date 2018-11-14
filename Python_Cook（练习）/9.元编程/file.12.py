# 9.12 利用装饰器给类定义打补丁

# 9.12.1 问题
# 我们想检查或改写一部分类的定义，一次来修改类的行为，但是不想通过继承或元类的方式来做
#　９．１２．２　解决方案


# 对于类装饰器来说这是绝佳的应用场景。比方说，下面有一个类装饰器重写了__getattribute__特殊方法，为其加上了日志日记功能


def log_getattribute(cls):
    print(cls)

    orig_getattribute = cls.__getattribute__

    def new_getattribute(self, name):
        print('geting:', name)

        return orig_getattribute(self, name)

    cls.__getattribute__ = new_getattribute

    return cls


@log_getattribute
class A:

    def __init__(self, x):
        self.x = x

    def spam(self):
        pass

a = A(66)
print(a.x)

# 9.12.3 讨论
# 类装饰器常常可以直接作为涉及混合类(mixin)或元类等高级技术的替代方案。例如，对于解决方案中的例子，另一种可选的实现方法是使用继承


class LoggedGetattribute:
    def __getattribute__(self, item):
        print('getting:',item)
        return super().__getattribute__(item)

# example
class A(LoggedGetattribute):
    def __init__(self,x):
        self.x = x

    def spam(self):
        pass

# 这么做是可行的，但是要想理解其中的原理，则必须对方法解析顺序(MRO),super(),以及其他有关继承方面的知识有所了解。从某种意义上说
# 类装饰器这种解决方案要更加直接。而且不会在继承体系中引入新的依赖关系。事实证明，由于不依赖对super()函数的使用，运行速度也会稍快一些

#  如果要将多个类装饰器作用域某个类之上，那么可能需要考虑添加的顺序问题。例如，如果某个装饰器是用全新的实现来替代一个类方法，而
#　另一个装饰器只是对已有的方法做包装，添加一些额外的逻辑处理，那么很可能需要先将第一个装饰器作用域类上。