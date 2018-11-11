# # 8.9 创建一种新形式的类属性或实例属性
#
# #  8.9.1 问题
# #  我们向创建一种新型是的实例属性，它可以拥有一些额外的功能，比如说类型检查。
# #  8.9.2  解决办法
# #  如果想创建一个新形式的实例属性，可以以描述符类的形式定义其功能，如下
# #  descriptor attribute for an integer type-checked attribute
#
# class Integer:
#     def __init__(self,name):
#         self.name = name
#
#     def __get__(self, instance, cls):
#         if instance is None:
#             return self
#         else:
#             return instance.__dict__(self.name)
#     def __set__(self, instance, value):
#         if not isinstance(value,int):
#             raise TypeError('Expected an int')
#         instance.__dict__(self.name) = value
#
#     def __delete__(self, instance):
#         del instance.__dict__(self.name)
#
#  所谓的描述符就是以特殊方法__get__(),__set__()和__delete__()的形式实现了3个核心的属性访问操作(对于get,set和delete)的类。这些方法
#　通过接受类实例作为输入来工作。之后，底层的实例字典会根据需要适当地进行调整

# 要使用一个描述符，我们把描述符的实例放置在类的定义中作为类变量来用。如下

# 每个描述符方法都会接受被操作的实例作为输入。要执行所请求的操作，底层的实例字典(__dict__属性)会根据需要适当地进行调整。描述符的self.name属性会保存
# 字典的键，通过这些键可以找到存储在实例字典中的实际数据

# 8.9.3 讨论
# 对大多数Ｐython类的特性，描述符都提供了底层的魔法，包括@classmethod,@staticmethod,@property甚至__slots__

# 通过定义一个描述符，我们可以在很底层的情况下捕捉关键的实例操作(get,set,delete),并可以完成自定义这些操作的行为
# 描述符常常作为一个组件出现在大型的编程框架中，其中还会设计装饰器或元类。如果只想访问某个特定的类中的一种属性，并对此定制化处理，那么
# 那么最好不要编写描述符来实现，对于这个认为，用property属性方法来实现会很简单,
# 在需要大量重用代码的情况下，描述符会更加有用

