# # #  示例15-2  测试LookingGlass 上下文管理器类
# #
# #
# from mirror import LookingGlass
# #
#
# with LookingGlass() as what:
#     print('A~~')
#     print(what)
#
# print(what)
#
# #  上下文管理器是LookingGlass类的实例:python在上下文管理器上调用__enter__方法,把返回结果绑定到what
#
# # 在实际使用中,如果应用程序接管了标准输出,可能会暂时把sys.stdout换成类似文件的其他对象,然后再切换成原来的版本
#
# # contextlib.redirect_stdout上下文管理器,只需传入类似文件的对象,用于替代sys.stdout
#
# # 解释器调用__enter__方法时，除了隐式的self之外，不会传入任何参数．传给__exit__方法的三个参数列举如下
#
# # 1.  exc_type  异常类
# #  2.  exc_value　异常实例．有时会有参数传给异常的构造方法，例如错误消息，这些参数可以使用exc_value.args获取
# # ３．　traceback   traceback对象
#
# # 上下文管理器的具体工作方式如下，在withZ块之外使用LookingGlass类，因此可以手动调动__enter__和__exit__方法
#
# # 示例１５－４　　在with块之外使用LookingGlass类
#

from mirror import LookingGlass

man = LookingGlass()
print(man)
mon = man.__enter__()
print(mon == 'AWERQAERQAWR')

#  在try/finanlly语句的finanlly块中调用sys.exc_info(),得到的是__exit__接收的这三个参数.鉴于with语句是为了取代大多数try/finanlly子句
#  而且通通常需要调用sys.exc_info()来判断做什么清理操作

#  15.3  contextlib模块中的使用工具

#  1. closing  如果对象提供了close()方法,但是没有实现__enter__/__exit__协议,那么可以使用这个函数构建上下文管理器

#  2. supppress  构建临时忽略指定异常的上下文管理器

#  3.@contextmanager  这个装饰器把简单的生成器函数变成上下文管理器,这样就不用创建类去实现管理器协议了
#  4.  ContextDecorator  这是个基类,用于定义基于类的上下文管理器.这种上下文管理器也能用于装饰器,在受管理的上下文中运行整个函数.

#  5.  ExitStack  这个上下文管理器能进入多个上下文管理器.with块结束时,ExitStack按照后进先出的顺序调用栈中各个上下问管理器的__exit__方法.
#  如果事先不知道with块要进入多少个上下文管理器,可以使用这个类.例如,同事打开任意一个文件列表中的所有文件


#  使用最多的是@contextmanager装饰器,这个装饰器与迭代无关,但是却要使用yield语句.由此引出了协程

#
