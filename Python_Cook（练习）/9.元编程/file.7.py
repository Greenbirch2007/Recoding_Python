#  9.7 利用装饰器对函数参数强制执行类型检查
#  9.7.1 问题
#  我们想为函数参数添加强制性的类型检查功能，将其作为一种断言或与调用者之间的契约

#  9.7.2  解决方案
#  在给出解决方案代码之前，本节的目标是提供一种手段对函数的输入参数类型做强制性的类型检查。


from inspect import signature
from functools import wraps


def typeassert(*ty_args,**ty_kwargs):
    def decorate(func):
        # if in optimized mode,disable type checking
        if not __debug__:
            return func

        # map function argument names to supplied types
        sig = signature(func)
        bound_types = sig.bind_partial(*ty_args,**ty_kwargs).arguments

        @wraps(func)
        def wrapper(*args,**kwargs):
            bound_values = sig.bind(*args,**kwargs)
            # enforce type assertions across supplied arguments
            for name,value in bound_values.arguments.items():
                if name in bound_types.arguments:
                    if not isinstance(value,bound_types.arguments[name]):
                        raise TypeError(
                            'Argument {} must be {}'.format(name,bound_types.arguments[name])
                        )
            return func(*args,**kwargs)
        return wrapper
    return decorate

# 我们会发现这个装饰器相当灵活，即允许指定函数参数的所有类型，也可以只指定一部分子集。此外，类型既能可以通过位置采纳数来制定，也可以
#  通过关键字参数来指定

#
# @typeassert(int,z=int)
# def spam(x,y,z=42):
#     print(x,y,z)

# spam(1,2,3)
# spam(6,6)
# spam(1,'hello',3)
# spam(1,'hello','world')

# 9.7.3  讨论
#  本节展示了一个高级的装饰器例子，引入了一些重要的概念

#  首先，装饰器的一个特性就是它们只会在函数定义的时候应用一次。在某些情况下，我们可能想禁止由装饰器添加的功能。为了做到这点
#  只要让装饰器函数返回那个未经包装的函数即可。在解决方案中，如果全局变量__debug__被设定为False。
#  下列代码就会返回未修改过的函数(当Python解释器-O或-OO的优化模式执行的话，则属于这猴子那个情况下)

#  接下来，编写这个装饰器比较棘手的地方在于要涉及对被包装函数的参数签名做检查。在这里，我们可选择的工具应该是inpsect.signature()函数
#  这个函数允许我们从一个可调用对象中提取出参数签名信息。如下


from inspect import signature

def spam(x,y,z=42):
    pass

sig = signature(spam)
# print(sig)
# print(sig.parameters)
# print(sig.parameters['z'].name)
# print(sig.parameters['z'].default)
# print(sig.parameters['z'].kind)

# 在装饰器实现的第一部分中，我们使用签名的bind_partial()方法对提供的类型到参数名做部分绑定。
bound_types=sig.bind_partial(int,z=int)
print(bound_types)
print(bound_types.arguments)

# 在这个部分绑定中，我们会注意到缺失的参数被简单地忽略掉了(即，这里没有对参数y做绑定)。但是，绑定过程中最重要的部分就是
#  创建了有序字典bound_types.arguments.这个字典将参数名以函数签名中相同的顺序映射到所提供的值上。
#  在我们的装饰器中，这个映射包含了我们打算强制施行的类型断言

#  在由装饰器构建的包装函数中用到了sig.bind()方法。bind()就如同bind_partial()一样，只是它不允许出现缺失的参数
#  因此，下面的示例中必须给出所有的参数

print(88*'~')
bound_values = sig.bind(1,2,3)
print(bound_values.arguments)

# 利用这个映射，要强制施行断言相对就很简单
for name,value in bound_values.arguments.items():
    if name in bound_types.arguments:
        if not isinstance(value,bound_types.arguments[name]):
            raise TypeError()

# 解决方案中一个微妙的地方是，对于具有默认值的参数，如果未提供参数，则断言机制不会作用在其默认值上。例如，
# 下面的代码可以工作，即使items的默认值是"错误"的类型

@typeassert(int,list)
def bar(x,items=None):
    if items is None:
        items = []
    items.append(x)
    return items

print(88*'&')

# 最后一点关于设计上的讨论应该就是装饰器参数与函数注解(function annotation)的对比了、例如，为什么不把装饰器实现为检查函数注解呢？

#不使用函数注解的一个可能原因在于函数每个参数只能赋予一个单独的注解。因此，如果把注解用于类型断言，则它们就不能用在别处。
# 此外，装饰器@typeassert不能用于使用了注解的函数还有一个原因。如同解决方案中展示的那样，通过使用装饰器参数，这个装饰器变得更加通用
# 可以用于任何函数————即使是使用了注解的函数也是如此