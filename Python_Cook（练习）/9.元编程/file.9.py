# #  ９．９　　把装饰器定义成类
# #  ９．９．１　问题
# #  我们想用装饰器来包装函数，但是希望得到的结果是一个可调用的实例。我们需要装饰器能在类中工作，也可以在类外部使用
#
# #  ９．９．２　　解决方案
# #  要把装饰器定义成类实例，需要确保咋类中实现__call__(),__get__()方法、例如，下面的代码定义了一个类，
# #  可以在另一个函数上添加一个简单的性能分析层
#
# import types
# from functools import wraps
#
#
# class Profiled:
#     def __init__(self,func):
#         wraps(func)(self)
#         self.ncalls = 0
#
#     def __call__(self, *args, **kwargs):
#         self.ncalls += 1
#         return self.__wrapped__(*args,**kwargs)
#     def __get__(self,instance,cls):
#         if instance is None:
#             return self
#         else:
#             return types.MethodType(self,instance)
#
# # 要使用这个类，可以像一个普通的装饰器一样，要么在类中要么在类外部使用：
#
#
# @Profiled
# def add(x,y):
#     return x+y
#
# class Spam:
#     @Profiled
#     def bar(self,x):
#         print(self,x)
#
# # 下面使用交互的方式，这些函数是如何工作的
#
# print(add(2,3))
# print(add(4,5))
#
# print(add.ncalls)
# s = Spam()
# s.bar(1)
#
# # 9.9.3 讨论
# # 把装饰器定义成类通常是简单明了的。但是，这里有一些相当微妙的细节值得做进一步解释，尤其是计划将装饰器用早实例的方法上时。
#
# # 1.首先，这里对functools.wraps()函数的使用和在普通装饰器中的目的一样————意在从被包装的函数中拷贝重要的元数据到可调用实例中
# # 2.其次，解决方案中所展示的__get__()方法常常容易被忽视。如果省略掉__get__()并保留其他所有的代码，会发现尝试
# # 调用被装饰的实例方法时会出现怪异的行为  如下
#
# # 出错的原因在于每当函数实现的方法需要在类中进行查询时，作为描述符协议(description protocol) 的一部分，它们的__get__()
# # 方法都会被调用，这部分内容在前面已经描述过，在这种情况下，__get__()的目的是用来创建一个绑定方法对象(最终会给方法提供self参数)
#
# s = Spam()
# def grok(self,x):
#     pass
# print(88*'1')
# print(grok.__get__(s,Spam))
#
# # 在本节中，__get__()方法在这里确保了绑定方法对象会恰当地创建出来。typeMethodType()手动创建一个绑定方法在这里使用。绑定方法
# # 只会使用到实例的时候才会被创建。如果在类中访问该方法，__get__()的instance参数就设为None,直接返回Profiled实例本身。
# # 这样就使得获取实例的ncalls属性成为可能
#
# # 如果想在某些方面避免这种混乱，可以考虑装饰器的替代方案。也即是使用闭包和nonlocal变量 如下
#
#
#
import types
from functools import wraps

def profiled(func):
    ncalls = 0
    @wraps(func)
    def wrapper(*args,**kwargs):
        nonlocal ncalls
        ncalls += 1
        return func(*args,**kwargs)
    wrapper.ncalls = lambda:ncalls
    return wrapper

# example
@profiled
def add(x,y):
    return x+y

# 这个例子使用起来和之前的方案几乎一样，除了现在访问ncalls时是以函数属性的形式来进行

print(add(2,3))
print(add(2,6))
print(add.ncalls)