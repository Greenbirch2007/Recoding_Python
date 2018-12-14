#　第12章 继承的优缺点

#　子类化内置类型和缺点
#　多重继承和方法解析顺序


#　12.1  子类化内置类型很麻烦


#　python2.2之后，内置类型可以子类化了，但是有个重要的注意事项：内置类型(使用C语言编写)不会调用用户定义的类覆盖的特殊方法

#　内置类型的方法不会调用子类覆盖的方法。例如，dict的子类覆盖的__getitem__()方法不会被内置类型的get()方法调用


# 示例 12.1  内置类型dict的__init__和__update__方法会忽略我们覆盖的__setitem__方法


# class DoppelDict(dict):
#     def __setitem__(self, key, value):
#         super().__setitem__(key,[value]*2)
#
#
# dd = DoppelDict(one=1)
# print(dd)
# dd['two']= 2
# print(dd)
# dd['three']= 3
# print(dd)
# dd1 = dict(one=1)
# print(dd1)
# dd1['two']= 2
# print(dd1)

# 原生类型的这种行为违背了面向对象编程的一个基本原则：始终应该从实例(self)所属的了开始搜索方法，即使在超类实现的类中调用也是如此
#　不只是实例内部的调用有这个问题(self.get()不调用self.__getitem__())，内置类型的方法调用的其他类的方法，如果被覆盖了，也不会被调用

# 示例１２．２　　dict.update方法会忽略AnswerDict.__getitem__方法


# class AnswerDict(dict):
#     def __getitem__(self, item):
#         return 42
#
# ad = AnswerDict(a='foo')
# print(ad)
# print(ad['a'])
# print(ad['a'])
# d ={}
# d.update(ad)
# print(d['a'])
# print(d)


# 示例１２．３　　扩展UserDict,

import collections

class DoppelDict2(collections.UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key,[value]*2)

dd = DoppelDict2(one=1)
print(dd)

dd['two']=2
print(dd)