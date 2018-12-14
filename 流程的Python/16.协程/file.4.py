# #　16.4  预激协程的装饰器
#
# #　如果不预激，那么协程没有什么用，调用ny_coro.send(x)之前，记住一定要调用next(my_coro)，为了简化协程的用法，有时使用一个预激装饰器
#
# # 预激协程的装饰器
#
# from functools import wraps
#
# def coroutine(func):
#     '''装饰器：向前执行到第一个'yield'表达式，预激'func''''
#     @wraps(func)
#     def primer(*args,**kwargs):
#         gen = func(*args,**kwargs)
#         next(gen)
#         return gen
#     return primer
#
# # 1. 把被装饰的生成器函数替换成这里的primer函数;调用primer函数时,返回预激后的生成器
# # 2. 调用被装饰的函数,获取生成器对象
# # 3. 预激生成器
# # 4. 返回生成器
#
#
# # 1.调用averager()函数创建一个生成器对象,在coroutine装饰器的primer函数中已经预激了这个生成器
# # 2. gergeneratorstate函数指明,处于GEN_SUSPENDED状态,因为这个协程已经准备好,可以接收值了
# # 3. 可以立即开始把值发给coro_avg--这正是coroutine装饰器的目的
# # 4. 导入coroutine装饰器
# # 5.把装饰器应用到averager函数上
#
#
# # 很多框架都提供了处理协程的特殊装饰器,不过不是所有装饰器都用于预激协程,有些会提供其他服务,例如勾入事件循环.比如说,异步网络库Tornado提供了tornado.gen装饰器
#
# # 使用yield from句法调用协程时,会自动预激.标准库中的asyncio.coroutine装饰器不会预激协程,因此能兼容yield from 句法
#
# # 协程的另一个重要特性---用于终止协程,以及在协程中抛出异常的方法
#
