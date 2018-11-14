# # #　9.11　编写装饰器为被包装的函数添加参数
# #
# # # 9.11.1  问题
# # # 我们想编写一个装饰器为被包装的函数添加额外的参数。但是，添加的参数不能影响到该函数已有的调用约定
# # # 9.11.2 解决方案
# # # 可以使用keyword-only 参数将额外的参数注入到函数的调用签名中。考虑如下的装饰器
# #
# #
# # from functools import wraps
# #
# # def optional_debug(func):
# #     @wraps(func)
# #     def wrapper(*args,debug=False,**kwargs):
# #         if debug:
# #             print('Calling',func.__name__)
# #         return func(*args,**kwargs)
# #     return wrapper
# #
# # # 测试上面的装饰器是如何工作的
# #
# # @optional_debug
# # def spam(a,b,c):
# #     print(a,b,c)
# #
# # spam(1,2,3)
# # spam(1,2,3,debug=True)
# #
# #
# # # 9.11.3 讨论
# # # 为被包装的函数添加额外的参数并不是装饰器最常见的用法。但是，对于避免某些特定的代码重复模式来书哦很有用。如下
# #
# # def a(x,debug=False):
# #     if debug:
# #         print('Calling a')
# #
# # def b(x,y,z,debug=False):
# #     if debug:
# #         print('calling b')
# #
# # def c(x,y,debug=False):
# #     if debug:
# #         print('calling c')
# #
# # # 可以对上面代码进行重构
# #
# # # @optional_debug
# # # def a(x):
# # #     pass
# # #
# # # @optional_debug
# # # def b(x,y,z):
# # #     pass
# # #
# # # @optional_debug
# # # def c(x,y):
# # #     pass
# #
# # # 这样的实现基于这样一个事实，即keyword-only参数可以很容易地添加到那些以*args,**kwargs作为形参的函数上。keyword-only参数会作为
# # # 特殊情况从随后的调用中挑选出来，调用函数时只会使用剩下的位置参数和关键字参数。
# #
# # # 在添加的参数和被包装函数的参数之间可能会出现潜在的名称冲突问题。例如，如果把@optional_debug装饰器作用到一个已经把debug作为参数的
# # # 函数上，词汇就会UI报错，所以需要添加额外的检查
#
#
# from functools import wraps
# import inspect
#
# def optional_debug(func):
#
#     if 'debug' in inspect.getargspec(func).args:
#         raise TypeError('debug argument already defined')
#
#     @wraps(func)
#     def wrapper(*args,debug=False,**kwargs):
#         if debug:
#             print('Calling',func.__name__)
#         return func(*args,**kwargs)
#     return wrapper
#
# # 本节最后一个需要考虑修改的地方在于如何恰当地管理函数签名。精妙的程序员会意识到被包装函数的签名是错误的。如下

from functools import wraps
import inspect


def optional_debug(func):
    if 'debug' in inspect.getargspec(func).args:
        raise TypeError('debug argument already defined')

    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print('Calling', func.__name__)
        return func(*args, **kwargs)

    sig = inspect.signature(func)
    parms = list(sig.parameters.values())
    parms.append(inspect.Parameter('debug',
                                   inspect.Parameter.KEYWORD_ONLY,
                                   default=False))
    wrapper.__signature__ = sig.replace(parameters=parms)
    return wrapper



# 修改之后，现在包装函数的签名就能正确反映出debug参数了

@optional_debug
def add(x,y):
    return x+y

print(inspect.signature(add))
print(add(2,3))