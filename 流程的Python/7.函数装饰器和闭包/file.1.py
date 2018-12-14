# 第7章  函数装饰器和闭包3
# 函数装饰器用于在源码中"标记"函数，以某种方式增强函数的行为。要掌握装饰器，要理解闭包

#　nonlocal是新近出现的保留关键字，如果要实现装饰器，就要熟悉nonlocal

#　除了在装饰器中有用之外，闭包还是回调式异步编程和函数式编程风格的基础

#　本章的模板是解释清楚装饰器的工作原理，包括最简单的注册装饰器，较复杂的参数化装饰器


#　python如何计算装饰器句法
#　python如何判断变量是不是局部的
#　闭包存在的原因和工作原理
#　nonlocal能解决什么问题


#　之后会探讨如下：
#　１．实现行为良好的装饰器　　　　２．　标准库中有用的装饰器　　　３．　实现一个参数化装饰器


#　７．１　　装饰器基础支持
#　装饰器是可调用的对象，其参数是另一个函数(被装饰器的函数)。装饰器可能会处理被装饰器的函数，然后把它返回，或将其替换成另一个函数或可调用对象


#　假设有一个deco装饰器

# @deco
# def target():
#     print('running target()')
#
# #　等价于
#
# def target():
#     print('running target()')
#
# target = deco(target)

# def add_3(num):
#     if num == int:
#         return (num + 3)
#     else:
#         print('出错')
#
#
# @add_3
# def add_6(num):
#     if num==int:
#         return  (num + 6)
#     else:
#         print('出错')
#
#
# print(add_6(6))

# 实例７．１　　　装饰器把函数替换成另一个函数


def deco(func):
    def inner():
        print('running inner()')
    return inner

@deco
def taret():
    print('running target()~~~~~~~~~')

taret()

# 严格的说，装饰器只是语法糖。装饰器可以像常规的可调用对象那样调用，其参数是另一个函数。有时候这样做更方便，比如做元编程(在运行是改变程序的行为)
# 综上，装饰器的一大特性是，能把被装饰的函数替换成其他函数。第二个特性，装饰器在加载模块时立刻执行

