# # 7.10 参数化装饰器
#
# # 创建一个装饰器工厂函数，把参数传递给它，返回一个装饰器，然后再把它应用要装饰的函数上
#
#
# # 示例7.22
# #
# # registry = []
# #
# #
# # def register(func):
# #     print('running register(%s)'% func)
# #     registry.append(func)
# #     return  func
# #
# #
# # @register
# # def f1():
# #     print('running f1()')
# #
# # print('running main()')
# # print('registry -->',registry)
# # f1()
#
# # # 输出如下
# # running register(<function f1 at 0x7fa2d2480510>)
# # running main()
# # registry --> [<function f1 at 0x7fa2d2480510>]
# # running f1()
#
#
#
#
# # 7.10.1  一个参数化的注册装饰器
# #　为了便于启用或禁用register执行的函数注册功能，我们为它提供一个可选的active参数，设为False，不注册被装饰的函数。从定义上
# # 这个新的register函数不是装饰器，而是装饰器工厂函数。调用它返回真正的装饰器，这才是应用到目标函数上的装饰器
#
# # 示例７．２３　为了接受参数，新的register装饰器必须作为函数调用
#
# registry = set()
#
# def register(activate=True):
#     def decorate(func):
#         print('running regsiter(activate=%s)->decorate(%s)'%(activate,func))
#         if activate:
#             registry.add(func)
#
#         else:
#             registry.discard(func)
#
#         return func
#     return decorate
#
#
# @register(activate=False)
# def f1():
#     print('running f1()')
#
# @register
# def f2():
#     print('running f2()')
#
# def f3():
#     print('running f3()')
#
#
# # 这里的关键是，register()要返回decorate,然后把它应用到被装饰的函数上

# 注意，只有f2在registry这种，如果想把f添加到registry中，则装饰f函数的句法registry()(f);不想添加(把它删除)的话，句法是register(activate=False)(f)