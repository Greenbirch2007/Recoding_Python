# 9.16  在*args 和　**kwargs上强制规定一种参数签名

# ９．１６．１　问题
# 我们已经编写了一个*args和**kwargs作为参数的函数或方法，这样使得函数成为通用型的(即，可可接受任意数量和类型的参数)。但是我们也想对传入的
# 参数做检查，看看它们是否匹配了某个特定的函数调用签名


# ９．１６．２　解决方案
# 任何关于操作函数调用签名的问题都应该使用inspect模块中的相应功能功能之类我们尤其感兴趣的是Signature,Parameter这两个类，
# 下面用一个交互的例子来说如何创建一个函数签名



from inspect import Signature,Parameter

# make a signature for a func(x,y=42,*,z=None)

parms = [Parameter('x',Parameter.POSITIONAL_OR_KEYWORD),
         Parameter('y',Parameter.POSITIONAL_OR_KEYWORD,default=42),
         Parameter('z',Parameter.KEYWORD_ONLY,default=None)]


sig = Signature(parms)
print(sig)

# 一旦有了签名对象，就可以通过对象的bind()方法轻松将其绑定到*args,**kwargs上，如下


def func(*args,**kwargs):
    bound_values = sig.bind(*args,**kwargs)
    for name,value in bound_values.arguments.items():
        print(name,value)

# try various example

# func(1,2,z=3)

# 可以看到，将签名对象绑定到传入的参数上会强制施行所有常见的函数调用规则，包括要求必须串的参数(如例子中的x),默认值，重复的参数等

# 关于强制施行函数签名，这里有一个更具体的例子，在代码中，基类定义了一二极其通用的__init__()方法，但是子类只提供一种期望接受的签名形式。


def make_sig(*names):
    parms = [Parameter(name,Parameter.POSITIONAL_OR_KEYWORD) for name in names]
    return Signature(parms)

class Structure:
   __signature__ = make_sig()
   def __init__(self,*args,**kwargs):
       bound_values = self.__signature__.bind(*args,**kwargs)
       for name,value in bound_values.arguments.items():
           setattr(self,name,value)

# example use

class Stock(Structure):
    __signature__ = make_sig('name','shares','price')

class Point(Structure):
    __signature__ = make_sig('x','y')


import inspect
print(inspect.signature(Stock))
s1 = Stock('apple',100,66.88)
print(s1)

# 9.16.3 讨论
# 当需要编写通用型的库，编写装饰器或实现代理时，使用形参为*args,**kwargs的函数非常常见。但是这种函数的一个缺点就是如果想实现自己的阐述检查机制；
# 代码会很混乱。如果使用自定义的元类来创建签名对象也是很有意义的，
# 当定义定制化的签名是，把签名对象保存到一个特殊的属性__signature__中常常很有用。如果这么做了，使用了inspect模块的代码在执行反射(introspection)
# 操作时将能够获取到签名并将其作为函数的调用约定。

