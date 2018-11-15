# # # ９．１８　通过编程的方式来定义类
# # # ９．１８．１　问题
# # # 我们编写的代码最终需要创建一个新的类对象。我们想到将组成类定义的源代码发送到一个字符串中，然后利用类似exec()这样的函数来执行，但是
# # # 我们希望能有一个更加优雅的解决方案
# # # ９．１８．２　解决方案
# # # 我们可以使用函数types.new_class()来实例化新的类对象。所有要做的就是提供类的名称，父类名称组成的元组，关键字参数以及一个用来
# # # 产生类字典(class dictionary)的回调，类字典中包含这类的成员。如下
# #
# #
# # # stock.py
# # # example of making a class manually from parts
# #
# # # methods
# #
# # class Stock():
# #     def __init__(self,name,shares,price):
# #         self.name = name
# #         self.shares = shares
# #         self.price = price
# #
# #     def cost(self):
# #         return self.shares * self.price
# #
# #     cls_dict = {
# #         '__init__' : __init__,
# #         'cost':cost,
# #     }
# #     # make a class
# #     import types
# #
# #     Stock = types.new_class('Stock',(),{},lambda ns:ns.update(cls_dict))
# #     Stock.__module__ = __name__
# #
# # s = Stock('apple',100,9.1)
# # # 在调用完types.new_class()之后对Stock.__module__的赋值操作是这个解决方案中的微妙之处。每当定义一个类时，其__module__属性中包含
# # # 的名称就是定义该类时所在的模块名。这个名称会用来为__repr__()这样的方法会输出，同事也会被各种库所用，比如pickle。因此为了让创建的类
# # # 成为一个"正常"的类，需要保证将__module__属性设置妥当
# # #　如果想创建的类还涉及一个不同的元类，可以在types.new_class()的第三个参数中进行指定
# #
# # #　new_class()的第四个参数最为神秘。它实际上是一个接受映射型对象的函数，用来产生类的命名空间。这通常都会是一个字典，但实际上可以是任何
# # #　由__prepare__()方法返回的对象。这个函数应该使用update()方法或其他的映射操作为命名空间中添加新的条目
# #
# # #　９．１８．３　　讨论
# # #　能够制造出新的类对象在某些特定的上下文中会有用。其中一个我们比较熟悉的例子和collections.namedtuple()函数有关。例如
# #
# # #　namedtuple()使用了exec(),但是，下面这个简单的函数可直接创建出类
# #
# #
#
# import operator
# import types
# import sys
#
# def named_tuple(classname,fieldnames):
#     # populate a dictionary of field property accessors
#     cls_dict = {name:property(operator.itemgetter(n)) for n,name in enumerate(fieldnames)}
#     # make a __new__ function and add to the class dict
#     def __new__(cls,*args):
#         if len(args) != len(fieldnames):
#             raise  TypeError('Expected {} arguments'.format(len(fieldnames)))
#         return tuple.__new__(cls,args)
#     cls_dict['__new__'] = __new__
#     # make the class
#     cls = types.new_class(classname,(tuple,),{},lambda ns:ns.update(cls_dict))
#     # set the module to that of the caller
#     cls.__module__ = sys._getframe(1).f_globals['__name__']
#     return cls
#
# # 上述代码的最后部分利用了所谓的“frame hack”技巧，通过sys._getframe()来获取调用者所在的模块名称。
#
# Point = named_tuple('Point',['x','y'])
# Point
# p = Point(4,5)
# print(len(p))
# print(p.x)
# print(p.y)
# print('%s %s'%p)
#
#
# # 本节使用的技术中一个重要的方面在于对元类提供了适当支持。我们可能会倾向于通过直接实例化一个元类来创建类。
# #　这种方法的问题在于它忽略了某些重要的步骤，比如调用元类的__prepare__()方法。通过采用types.new_class(),可以保证所有必要的初始化步骤都
# #　能得到执行。例如，在types.new_class()中给定的第四个参数是一个回调函数，它所接受的映射型对象正是由__prepare__()方法返回的
#
# #　这么做会找的合适的元类并调用它的__prepare__()方法。元类，剩下的关键字参数以及准备好的命名空间都得到返回
#
# # 可见，执行顺序为：
# # prepare（创建命名空间）-> 依次执行类定义语句 -> new（创建类）-> init（初始化类）
# # 元类定义了prepare以后，会最先执行prepare方法，返回一个空的定制的字典，然后再执行类的语句，类中定义的各种属性被收集入定制的字典，最后传给new和init方法。
#
# # 新式类继承：广度优先。
# #
# # 经典类继承：深度优先。
# #
# # 继承了object的类以及其子类，都是新式类
# # 没有继承object的类以及其子类，都是经典类
# # Python3中默认继承object，所以Python3中都是新式类
#
# 新式类：直接或者间接（子类的父类，爷爷类..祖师爷类继承
#
# object也算间接）继承object类称为新式类
# Python2.7 中没有显式继承object就不是新式类，必须这样写：
# class A(object)才是继承object类
#
# Python3中默认继承object类
# 新式类的继承 查找 顺序是：广度优先
# class D(object)
# class C1(D)
# class C2(D)
# class B(C1,C2)
# class A(B,C1,C2):继承 查找 顺序是：A->B->C1->C2->D->object