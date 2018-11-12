# # 8.13  实现一种数据模型或类型系统
#
# # 8.13.1  问题
#
# # 我们想定义各各种各样的数据结构，但是对于某些特定的属性，我们想对允许赋给它们的值强制添加一些限制
#
# # 8.13.2  解决方案
#
# # 基本上我们面对的任务就是在设定特定的实例属性时添加检查或断言。需要对每个属性的设定做定制化处理，因此应该使用描述符来完成
#
# # 可以运用一些技术来简化在类中设定约束的步骤。一种方法是使用类装饰器，
#
# # class decorator to apply constrains
#
# def check_attribute(**kwargs):
#     def decorate(cls):
#         for key,value in kwargs.items():
#             if isinstance(value,D):
#                 value.name = key
#                 setattr(cls,key,value)
#             else:
#                 setattr(cls,key,value(key))
#         return cls
# return decorate
#
# # 另一种方法是使用元类
#
class checkedmeta(type):
    def __new__(cls, *args, **kwargs):
        pass

# 8.13.3 讨论
# 本节涉及了好几种高级技术，包括描述符，mixin类，对super()的使用，类装饰器以及元类
# 实现类装饰器和元类的代码会扫描类字典，寻找描述符。当找到描述符后，它们会根据键的值自动填入描述符的名称
# 在所有方法中，类装饰器可以提供最大的灵活性和稳健性。第一个，这候总解决方案不依赖于任何高级的机制，比如元类
# 第二，装饰器可以很容易地根据需要在类定义上添加或移除。例如，在装饰器中，可以有一个选项来简单地忽略掉添加的检查机制。这样
# 就能让检查机制可以根据需要随意打开或关闭(调试环境对比生产环境)
# 最后，采用类装饰器的解决方案也可以用来取代mixin类，多重继承以及对super()函数的使用