#　８．16  在类中定义多个构造函数

#　８．１６．１　问题
#　我们正在编写一个类，但是想让用户能够以多种方式创建实例，而不局限与__init__()提供的这一种

#　８．１６．２　　解决方案
#　要定义一个含有多个构造函数的类，应该使用类方法，如下

import time

class Date:
    #primary constructor
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day

    # alternate constructor
    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year,t.tm_mon,t.tm_day)

# 要使用这个备选的构造函数，只要把它当做函数来调用即可，如 Date.today(). 如下

# ８．１６．３　讨论
# 类方法的一大主要用途就是定义其他可选的构造函数。类方法的一个关键特性就是把类作为其接收的第一个参数(cls).我们会注意到，类方法
# 中会用到这个类来创建并返回最终的实例。但是这一特性使得类方法能够在继承中被正确使用

# 当定义一个有着多个构造函数的类时，应该让__init__()函数尽可能简单————除了给属性赋值职位什么都不做。如果需要的话，可以在其
#　他备选的构造函数中选择实现更高级的操作。与单独定义一个类方法不同的是，我们可能会倾向于让__init__()方法支持不同的调用约定