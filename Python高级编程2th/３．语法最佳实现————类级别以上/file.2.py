#  ３．２．１　python2中的旧式类与super
#  python2中super()的工作原理几乎完全相同。调用签名的唯一区别在于简化的领参数形式不可用，因此必须始终提供至少一个参数
#  python2中的super只适用于新式类，如果类的定义中没有指定祖先，那么它就会被解释为旧式类，且不能使用super

class OldStyle1:
    pass

class OldStyle2:
    pass

#  python 2中的新式类必须显式继承object或其他新式类

class NewStyleClass(object):
    pass

class NewStyleClassToo(NewStyleClass):
    pass

#  python3不再保留旧式类的概念，因此，没有继承任何其他类的类都隐式地继承自object。显式声明表明某个类继承自object似乎是冗余的。
#  通用的良好实践是不包括冗余代码。只有项目不再用于任何python2版本时，删除这些冗余才是好的做法。如果代码想要保持python的跨版本兼容
#  那么必须始终将object作为所有基类的祖先


#  ３．２．２　理解python的方法解析顺序
#  python的方法解析顺序是基于C3，它描述了C3如何构建一个类的线性化(也叫优先级，即祖先的有序列表)。这个列表可用于属性查找
#  MRO的变化是用于解决创建公共基本类型(object)所引入的委托。在使用Ｃ３线性方法之前，如果有一个类有两个祖先，那么对于不使用多重继承模型的
#  简单情况，方法解析顺序的计算和跟踪都很简单


# class Base1:
#         print('Base2')
#
# class Myclass(Base1,Base2):
#     pass
#
# Myclass().method()
#
#     pass
#
# class Base2:
#     def method(self):


#  python3中所有类都具有相同的共同祖先，由于使用现有MRO使其正常工作要花费太多的精力，所以提供一个新的MROＧＥＮＧＪＩＡＮＤＡＮ

class CommonBase:
    def method(self):
        print('CommonBase')

class Base1(CommonBase):
    pass

# class Base2(CommonBase):
#     def method(self):
#         print('Base2~')
class Base3(CommonBase):
    def method(self):
        print('Base3~')
class Base6(CommonBase):
    def method(self):
        print('Base6~')

class MyClass(Base1,Base3,Base6):
    pass
MyClass().method()
# 这种用法，C3序列化会挑选最接近的祖先的方法m

# Python　MRO是基于对基类的递归调用，


# L[MyClass(Base1,Base2)]= MyClass + merge(L[Base1],L[Base2],Base1,Base2)

# 这里L【ＭyClass】是MyClass类的线性化，而merge是合并多个线性结果的具体算法
# Ｃ的线性化是Ｃ加上父类的线性话和父类列表的合并的总和。
# merge算法负责删除重复项并保持正确的顺序。#取第一个列表的表头(head).即L[Base1][0].如果这个表头不在其他任何列表
# 表尾(tail)，那么就将它添加到Myclass的线性化中，并从合并的列表里删除；否则，查看下一个列表的表头，如果是一个好的表头
# 就将其取出。然后重复这一动作，直到所有的类都被删除或找不到好的表头位置
# head(表头)是列表的第一个元素，而tail（表为）则包含其余元素。例如，在(Base1,...BaseN)中，Base1,是head,剩下的是tail

# C3对每个父类进行递归深度查找以得到一个列表序列。然后，如果某个类包含在多个列表中，它会利用层次结构消歧(hierarchy disambiguation)
# 计算出从做到右的规则，一次合并所有的列表
#　类的__mro__属性(只读)保存了线性化的计算结果，这在加载类定义时已经完成
#　３．２．３　使用super易犯的错误

#　现在回到super,如果使用了多重继承的层次结构，那么使用super是非常唯一的，主要原因在于类的初始化。在python中，
#　基类不会在__init__()中隐式地调用，所以需要由开发人员来调用它们

#　1. 混用super与显式类调用

class A:
    def __init__(self):
        print('A',end=' ')
        super().__init__()

class B:
    def __init__(self):
        print('B',end=' ')
        super().__init__()

class C(A,B):
    def __init__(self):
        print('C',end=' ')
        A.__init__(self)
        B.__init__(self)
print('MRO:',[x.__name__  for x in C.__mro__])
C()
# Ｃ的实例调用A.__init__(self),因此使得super(A,self).__init__()调用了B.__init__()方法。super应该被用到整个类
#　的层次结构中。问题在于，有时这种层次结构的一部分位于第三方代码中。
#　你无法确定外部包的代码是否使用了super()。如果你需要对某个第三方类进行子类化，最好总是查看其内部代码以及MRO中其他类的内部代码

#　２．　不同种类的参数
#　使用super