# 8.7

# 8.7.1 问题
# 我们想调用一个父类中的方法，这个方法在子类中一斤被覆盖了
# 8.7.2  解决方案
# 要调用父类(或超类)中的方法，可以使用super()函数完成。如下


class A:
    def spam(self):
        print('A.spam')

class B:
    def spam(self):
        print('B.spam')
        super().spam()  # call parent spam()

# super()函数的一种常见用途是调用父类的__init__()方法，确保父类被正确地初始化了。


class A:
    def __init__(self):
        self.x = 0

class B:
    def __init__(self):
        super().__init__()
        self.y = 1

# 另一种常见用途是当覆盖了Pythono中的特殊方法时，如下


class Proxy:
    def __init__(self,obj):
        self._obj = obj

    # delegate attribute lookup  to internal obj

    def __getattr__(self, name):
        return getattr(self._obj,name)

    # delete attribute assignment

    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name,value)  #  call original __setattr__
        else:
            setattr(self.obj,name,value)


# 在上述代码中，__setattr__()的实现里包含了对名称的检查。如果名称是以一个下划线(_)开头的，它就是通过super()去调用原始的__setattr__()实现。
# 否则，就转而对内部持有的对象self._obj 进行操作。但是super()即使在没有显式列出基类的情况下也是可以工作的。

# 8.7.3  讨论
# 如何正确使用super()函数，这实际上是人们在Python中理解的最差的知识之一。偶尔我们会看到一些代码直接调用父类中的方法




# 如果运行上面的代码，会发现Base.__init__()方法被调用了两次。如下

# c = C()
# c


# 如果从另一个方面考虑，将代码修改为使用super()，那么一切就能正常工作了

#
# class Base:
#     def __init__(self):
#         print("Base.__init__")
#
# class A(Base):
#     def __init__(self):
#         super().__init__()
#         print('A.__init__')
#
#
# class B(Base):
#     def __init__(self):
#         super().__init__()
#         print('B.__init__')
# class C(A,B):
#     def __init__(self):
#         super().__init__()  # only one call to super() here
#         print('C.__init__')
#
# c = C()
# c

# 当使用这个新版的代码时，就会发现每个__init__()方法都只调用了一次

# 要理解其中的原油，先看Python是如何实现继承的。针对每一个定义的类，Python都会计算出一个称为方法解析顺序(MRO)的列表。
# 实际上是以Python元组来表示的，因为__mro__属性是只读的
# MRO列表只是简单地对所有的基类进行线性排列 ，如下


# print(C.__mro__)
# 要实现继承，Python从MRO；列表中最左边的类开始，从左到右依次查找，直到找到待查的属性时为止。
# 而MRO列表本身又是如何确定的呢？这里用到了一种C3线性化处理(C3Linearization)的技术。针对父类的一种归并排序，它需要满足3个约束：
# 1.先检查子类再检查父类
# 2.有多个父类时，按照MRO列表的顺序依次检查
# 3.如果下一个待选的类出现了两个合法的选择，那么就从第一个父类中选取
#所有需要的知道的就是MRO；列表中对类的顺序几乎适用于任何定义的类层次结构(class hierarchy)

# 当使用super()函数时，Ｐython会继续从MRO中的下一个类开始搜索。只要每一个重新定义过的方法(也就是覆盖方法)都使用了super(),
# 并且只调用了它一次，那么控制流最终就可以遍历整个MRO列表，并且让每个方法只会被调用一次。这就是为什么在第二个例子中Ｂ.__init__()不会被
# 调用两次的原因

# 关于super(),它不是一定要关联到某个类的直接父类上，甚至可以在没有直接父类的类中使用它。如下

class A:
    def spam(self):
        print('A.spam')
        super().spam()

class B:
    def spam(self):
        print('B.spam')




class C(A,B):
    pass

c = C()
c.spam()
print(C.__mro__)

# 这里我们会发现在类中使用的super().spam()实际上居然调用到了类中的spam()方法————Ｂ和Ａ是完全不相关的。这一切都可以用类C的ＭＲＯ列表来解释

# 但是，由于super()可能会调用到我们不希望调用的方法，那么这里要有一些基本准则
#  首先，确保在继承体系中所有同名的方法都有可兼容的调用签名(即，参数数量相同，参数名称也相同)。如果super()尝试取调用非中介父类的方法
#  其次，确保最顶层的类实现了这个方法是个好主意，这样沿着MRO列表展开的查询链会因为最终找到了实际的方法而终止
