# # 　第２１章　类元编程
#
#
# # 类元编程是指在运行时创建或定制类的技巧．在python中，类是一等对象，因此任何时候都可以使用函数新建类，而无需使用class关键字．
# #  类装饰器也是函数，不过能够审查，修改，甚至把被装饰的类替换成其他类．最后元类是类元编程最高级的工具：
# #  使用元类可以创建具有某种特质的全新勒种，例如抽象基类
#
#
# #  21.1  类工厂函数
#
# #  标准库中有一个类工厂函数---collections.namedtuple.我们把一个类名和几个属性名传给这个函数，它会创建一个tuple的子类,其中
# #  的元素通过名称获取，还为调试提供了友好的字符串表示形式(__repr__)
#
#
# #  可以创建一个类似的工厂函数，用于创建可变对象
#
#
# # 示例２１－１　　测试recode_factory函数，一个简单的类工厂函数
#
# from record_factory import record_factory
#
# Dog = record_factory('Dog',' name weight owner') # 1. 这个工厂函数的签名与namedtupled类似：先写类名，后面跟着写一个字符串里的多个属性名，使用空格或逗号分开
# rex = Dog('Rex',30,'Bob')
# print(rex)# 2.友好的字符串表示形式
#
# name,weight,_ = rex  # 3. 实例是可迭代的对象，因此赋值时可以便利的拆包
# print(name)
# print(weight)
#
# print(88*'~')
#
# t = "{2}'s dog weighs {1}kg".format(*rex) # 4. 传给format等函数时也可以拆包
# print(t)
# rex.weight = 88 # 记录实例是可变的对象
#
# print(rex)
# print(Dog.__mro__) # 6.新建的类继承自object,与我们的工厂函数没有关系
#
# #  通常,我们把type视作函数,因为也是像函数那样调用它的.例如,调用type(my_object)获取对象所属的类---作用与my_object.__class__相同.
# #  然而,type是一个类.当成类使用时.传入三个参数可以新建一个类
#
# MyClass = type('MyClass',(MySuperClass,MYMixin),
#                {'x':42,'x2':lambda self:self.x*2})
#
# # type的三个参数分别是name,bases和dict.最后一个参数是一个映射,指定新类的属性名和值. 上述代码可以写成如下形式
#
#
# class MyClass(MySuperClass,MYMixin):
#     x = 42
#
#     def x2(self):
#         return self.x *2
#
#
#
# #　type的实例是类，例如这里的MyClass类或Dog类
# # record_factory函数的最后一行会构建一个类，类的名称是cls_name参数的值，唯一的直接超类是object,有__slots__,__init__,
# #  __iter__和__repr__四个类属性，其中三个是实例方法
#
# #  使用__setattr__方法，为属性赋值时验证属性的名称
#
# #  在python中做元编程时，最好不要用exec和eval函数，
#
# #  record_factory函数创建的类，有一个局限性，不能序列化．即不能使用pickle木块的dump/load函数处理
#
# #  ２１．２　　定制描述符的类装饰器
#
#
# #  如果存储属性的名称中包含托管属性的名称更好
# #  要在创建类时设置存储属性的名称．使用类装饰器或元类可以做到这一点
# #  类装饰器和函数装饰器很相似，是参数为类对象的函数，返回原来的类或修改后的类
#
# #  示例２１－３　　解释器会计算LineItem类，把返回的类对象传给model.entity函数．python会把LineItem这个全局名称绑定给model.entity函数
# #  返回的对象．model.entity函数会返回原先的LineItem类，但是会修改各个描述符实例的storage_name属性
#
# #  示例２１－３　　使用Quantity和NonBlank描述符的LineItem类
#
import model_v6 as model

@model.entity # 1.增加了类装饰器
class LineItem:
    description = model.NonBlank()# 使用mode.NonBlank描述符，其他代码没变
    weight = model.Quantity()
    price=  model.Quantity()


    def __init__(self,desciption,weight,price):
        self.description = desciption
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


ra = LineItem('Golan',10,69)
print(dir(ra))

# 类装饰器能以简单的方式做到以前需要使用元类去做的是---创建类时定制类

# 类装饰器有一个重大缺点:支队直接依附的类有效.这意味着,被装饰器的类子类可能继承也可能不继承装饰器所做的变动

#　２１．３　　导入时和运行时比较

#　２１．４　　元类基础知识


#　元类是生产机器的机器