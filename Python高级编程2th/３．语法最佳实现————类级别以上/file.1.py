# # 　第３章　语法最佳实践————类级别以上
# # 本章概述了用于操作和改进类代码的python高级语法。python3只用新式类模型
#
# # 本章的主题　
# # １．　子类化内置类型　　２．　访问超类中的方法　　３．　　使用property和槽(slot)  4. 元编程
#
#
# # ３．１　　子类化内置类型
# # python的子类化内置类型偶一个object的内置类型，它是所内置类型的共同祖先，也是所有没有显式指定父类的用户自定义类的共同祖先。
# # 每当需要实现与某个内置类型具有相似香味的类时，最好的方法是将这个内置类型子类化
#
# # 现在展示一个名为distinctdict类的代码，它就使用了这猴子那个方法。它是python中普通的dict类型的子类。这个新类的大部分
# # 行为与普通的dict相同，但它并不允许多个键对应相同的值。如果有人试图添加具有相同值的新元素，那么会引发一个valueError的子类，并给出一些帮助的信息
#
#
# class DistinctError(ValueError):
#     '''如果向distinctdict添加重复值，则引发这个错误。'''
#
# class distinctdict(dict):
#     '''不接受重复值的字典。'''
#     def __setitem__(self, key, value):
#         if value in self.values():
#             if (
#                     (key in self and self[key] != value) or key not in self
#             ):
#                 raise DistinctError('This value already exists for different key')
#
#         super().__setitem__(key,value)
#
#
#
# my = distinctdict()
# my['key']= 'value'
# my['other_key'] = 'value'
#
# print(my)
#
# # 如果查看现有的代码，你坑呢会发现都是对内置类型的部分实现，他妈妈作为子类的速度更快，代码更简洁
# # 例如，list类型用来管理序列，如果一个类需要在内部处理序列，那么就可以对list进行子类化，如下
#
#
# class Folder(list):
#     def __init__(self,name):
#         self.name = name
#     def dir(self,nesting=0):
#         offset = " " * nesting
#         print('%s%s/ '%(offset,self.name))
#
#         for element in self:
#             if hasattr(element,'dir'):
#                 element.dir(nesting + 1)
#             else:
#                 print('%s %s'%(offset,element))
#
# tree =  Folder('project')
# tree.append('README.md')
# tree.dir()

# 内置类型覆盖了大部分使用场景
# 如果打算创建一个与序列或映射类似的新类，应考虑其特性并查看现有的内置类型，除了基本内置类型，collections模块还额外提供了许多有用的容器
# 大部分情况下最终会使用它们
# ２．　访问超类中的方法
# super是一个内置类，可以用于访问属于某个对象的超类的属性。
# 如果你已经习惯于直接调用父类并传入self作为第一个参数来访问类的属性或方法，super的方法比较成就


class Mama:  # 旧的写法
    def says(self):
        print('do your homework')

# class Sister(Mama):
#     def says(self):
#         Mama.says(self)
#         print('and clean your bedroom')


# 重点看一下Mama.says(self)这一行，这里我们使用刚刚提到的方法来调用超类(即Mama类)says()方法，并将self作为参数传入。
# 调用的是属于Mama的says()方法。但它的作用对象由self参数给出，在这个例子中是一个Sister实例

# super的用法如下

class Sister(Mama):
    def says(self):
        super(Sister,self).says()
        print('and clean your bedroom')

#　或者，如下

# class Sister(Mama):
#     def says(self):
#         super().says()
#         print('and clean your bedroom')
#

# super的简化形式(不传入任何参数)可以在方法内部使用，但super的使用并不限于方法。在代码中需要调用给定实例的超类方法的任何地方都可以使用它。
# 不过，如果super不再方法内部使用，那么必须给出如下参数

anita = Sister()
super(anita.__class__,anita).says()

# 最后，关于super要注意，就是它的第二个参数是可选的。如果只提供了第一个参数，那么super返回的是一个未绑定(unbound)类型
# 这一点在于classmethod一起使用时特别有用，如下


print(88*'~')

class Pizza:
    def __init__(self,topping):
        self.topping = topping

    def __repr__(self):
        return 'Pizza with ' + 'and '.join(self.topping)

    @classmethod
    def recommend(cls):
        '''推荐任何馅料(topping)的某种披萨'''
        return cls(['spam','ham','eggs'])


class VikingPizza(Pizza):
    @classmethod
    def recommend(cls):
        '''推荐与super相同的内容，但多加了午餐肉(spam)'''
        recommeded = super(VikingPizza).recommend()
        recommeded.topping += ['spam'] *5
        return recommeded

#  注意，零参数的super()形式也可用于被classmethod装饰器装饰的方法。在这样的方法中无参数调用的super()被看做是仅定义了第一个参数
#  前面提到的使用实例很容易理解，但是如果面对多重继承模式，super将变得难以使用。解释这些问题之前，理解何时赢避免使用super以及
#  方法解析顺序(Method Resolution Order,MRO)在python中的工作原理很重要

#