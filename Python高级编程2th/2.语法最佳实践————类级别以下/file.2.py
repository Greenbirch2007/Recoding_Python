# # # # #  4. 超越基础集合类型——————collections模块
# # # #
# # # # # 每种数据结构都有缺点。没有一种集合类型适合解决所有问题，4种基本类型(元组，列表，集合和字典)提供的选择不算多。python的标准库collections还提供了其他选择
# # # # # 1.namedtuple():用于创建元组子类的工厂函数(factory function),可以通过属性名来访问它的元索引
# # # # # 2. deque:双端队列，类似列表，是栈和队列的一般化，可以在两端快速添加或取出元素
# # # # # 3. ChainMap:类似字典的类，用于创建多个映射的单一视图
# # # # # 4. OrderedDict:字典子类，可以保存元素的添加顺序
# # # # # 5. defaultdict:字典子类，可以通过调用用户自定义的工厂函数来设置缺失值
# # # #
# # # # # 2.2  高级语法
# # # # #  迭代器(iterator)  生成器(generator)   装饰器(decorator)   上下文管理器(context manager)
# # # #
# # # # # 2.2.1  迭代器
# # # # # 迭代器只不过是一个实现了迭代器协议的容器对象。它基于以下两个方法：
# # # # # 1.   __next__:返回容器的下一个元素
# # # # # 2.  __iter__:返回迭代器本身
# # # # # 迭代器可以利用内置的iter函数和一个序列来创建。
# # # #
# # # # i = iter('abc')
# # # # print(next(i))
# # # # print(next(i))
# # # # # print(next(i))
# # # # # print(next(i))
# # # #
# # # # # 当遍历完序列时，会引发一个StopIteration异常。这样迭代器就可以与循环因为可以捕捉这个异常并停止循环。要创建自定义的迭代器，可以便携仪更具有
# # # # #　__next__()方法的类，只要这个类提供返回迭代器实例的__iter__的特殊方法
# # # #
# # # # class CountDown:
# # # #     def __init__(self,step):
# # # #         self.step = step
# # # #     def __next__(self):
# # # #         '''Return the next element.'''
# # # #         if self.step <= 0:
# # # #             raise StopIteration
# # # #         self.step -= 1
# # # #         return self.step
# # # #     def __iter__(self):
# # # #         ''''Return the iterator itself.'''
# # # #         return self
# # # # #
# # # # # for e in CountDown(60):
# # # # #     print(e)
# # # #
# # # # #　迭代器本身是一个底层的特性和概念，在程序中可以不用它。但它为生成器这的特性提供了基础
# # # # #　２．２．２　　yield 语句
# # # # #　生成器提供了一个更加优雅的方法，可以让编写返回元素序列的函数所需的代码变得简单，高效，基于yield语句，生成器可以暂停函数并返回一个中间结果。
# # # # #　该函数会保存执行上下文，稍后在必要时可以恢复
# # # #
# # # # #　斐波那契数列可以用生成器语法来实现
# # # #
# # # # def fibonacci():
# # # #     a,b = 0,1
# # # #     while True:
# # # #         yield b
# # # #         a,b = b,a+b
# # # # # 你可以用next()函数或for循环从生成器中取新的元素，就像迭代器一样
# # # # fib = fibonacci()
# # # # print(next(fib))
# # # #
# # # # # 这个函数返回一个generator对象，特殊的迭代器，它知道如何保存执行上下文。它可以被无限次调用，每次都会生成序列的下一个元素。
# # # # # 这种算法可无限调用的形式并没有影响ｄｉａｍ的可读性，不必提供使函数停止的方法。实际上，它看上去就像伪代码设计的数列一样
# # # # # 在社区中，生成器并不常用，但是你每次需要返回一序列的函数或在循环中运行函数时，都应该考虑使用生成器。当序列元素被传递到
# # # # # 另一个函数中以进行后续处理是，一此返回一个元素可以提高整体性能
# # # # # 在这种情况下，用于处理一个元素的资源通常不如用于整个过程的资源重要，因为它们可以保持位于底层，使程序更加高效。
# # # # # 一个常见的应用场景是使用生成器的数据流缓存区。使用这些数据的第三方代码可以暂停，恢复和停止生成器，在开发这一过程之前无需导入所有数据
# # # # # 举例，来自标准库的tokenize模块可以从文本流中生成令牌(token),并对处理过得每一行都返回一个迭代器，以供后续处理
# # # #
# # #
# # # # import tokenize
# # # # reader = open('hello.py').readline()
# # # # tokens = tokenize.generate_tokens(reader)
# # # # print(next(tokens))
# # #
# # # # open遍历文件的每一行，而generate_tokens则利用管道对其进行遍历，完成一些额外假的工作。对于基于某些序列的数据转换算法而言，生成器还
# # # # 有助于降低算法复杂度并提高效率。把每个序列看做一个iterator,然后再将其合并为一个高阶函数，这种方法可以有效避免变得没有可读性。
# # # # 此外，这种方法可以为整个处理链提供实时反馈。
# # #
# # # # 在下面的例子中，每个函数都定义了一个对序列的转换。然后将这些函数链接起来应用。每次调用都将处理一个元素并返回其结果
# # # from functools import wraps
# # #
# # #
# # # def power(values):
# # #     for value in values:
# # #         print('powering %s' % value)
# # #         yield value
# # #
# # # def adder(values):
# # #     for value in values:
# # #         print('adding to %s'% value)
# # #         if value % 2 ==0:
# # #             yield value + 3
# # #         else:
# # #             yield  value + 2
# # #
# # # # 将这些生成器合并使用。
# # #
# # # element = [1,4,7,9,12,19]
# # # results = adder(power(element))
# # # print(next(results))
# # #
# # # # 保持代码简单，而不是保持数据简单
# # # # 最好编写多个处理序列值的简单可迭代函数，而不要编写一个复杂函数，同时计算出整个集合的结果。
# # # # ｐython生成器的另一个重要特性，就是能够利用next函数与调用的代码进行交互。yield变成了一个表达式，而值可以通过名为send的新方法来传递
# # #
# # # # def psychologist():
# # # #     print('Please tell me your problem')
# # # #     while True:
# # # #         answer  = (yield )
# # # #         if answer is not None:
# # # #             if answer.endwith('?'):
# # # #                 print("Don't ask yourself too much questions ")
# # # #             elif 'good' in answer:
# # # #                 print('Ahh that is a good,go on')
# # # #             elif 'bad' in answer:
# # # #                 print('do not be so negative')
# # # #
# # # # free = psychologist()
# # # # print(next(free))
# # #
# # # # send的作用和next类似，但会将函数定义内部传入的值变成yield的返回值，因此，这个函数可以根据客户端代码来改变自身行为。为完成这行为，
# # # # 还添加了另外两个函数:throw, close,它们将向生成器抛出错误
# # # # 1. throw:允许客户端ｄｉａｍ发送要跑车的任何类型的异常
# # # # 2. close :作用相同，但会引发特定的异常————GeneratorExit.这种情况下，生成器函数必须再次引发GeneratorExit或StopIteration
# # # # 生成器是python中协程，异步并发等其他概念的基础
# # #
# # # # 2.2.3 装饰器
# # #
# # # # python装饰器的作用是使函数包装与方法包装(一个函数，接受函数并返回其增强函数)变得更容易阅读和理解。最初的使用场景是在方法定义
# # # # 的开头能够将其定义为类方法或静态方法，如果不用装饰器语法，就很繁琐
# # #
# # # class WithoutDecorators:
# # #     def some_static_method():
# # #         print('this is static method')
# # #     some_static_method = staticmethod(some_static_method)
# # #
# # #     def some_class_method(cls):
# # #         print('this is class method')
# # #     some_class_method = classmethod(some_class_method)
# # #
# # #
# # # # 如果使用装饰器语法重写，代码就更加简洁
# # #
# # # class WI:
# # #     @staticmethod
# # #     def some_static_method():
# # #         print('a')
# # #
# # #     @classmethod
# # #     def some_class_method(cls):
# # #         print('c')
# # #
# # #
# # # # 1.一般语法和可能的实现
# # # # 装饰器通常是一个命名的对象(不允许使用lambda表达式)，在被(装饰函数)调用时接受单一参数，并返回另一个可调用对象。装饰器通常在方法和函数的范围讨论
# # # #　但是实际上，任何可调用对象(任何实现了__call__方法的对象都是可调用的)都可以用作装饰器，它们返回的对象往往不是简单的函数，而是实现了自己的__call__方法更复杂的类的实例
# # # # 装饰器语法只是语法糖而已，
# # #
# # # # 装饰器甚至不需要返回可调用对！事实上，任何函数都可以用作装饰器，因为python诶呦规定装饰器的范湖类型。
# # #
# # # # (1)作为一个函数
# # # # 编写自定义函数装饰器有很多方法但最简单的方法就是编写一个函数，返回包装原始函数调用的一个子函数
# # #
# # # def mydec(function):
# # #     def wrapped(*args,**kwargs):
# # #         # 在调用原始函数之前，做点什么
# # #         res = function(*args,**kwargs)
# # #         # 在调用之后，做点什么
# # #         # 并返回结果
# # #         return results
# # #     # f返回 wrapper作为装饰函数
# # #     return wrapped
# # #
# # #
# # # # (2) 作为一个类
# # # # 虽然装饰器几乎总是可以用函数实现，但是有些情况下，使用用户自定义类可能更好。如果装饰器需要复杂的参数haunted或依赖于特定状态，那么
# # # # 这种说法是正确的。 非参数化装饰器用作类的通用模式如下
# # #
# # # class Dec:
# # #     def __init__(self,function):
# # #         self.function = function
# # #
# # #     def __call__(self, *args, **kwargs):
# # #         # 在调用原始函数之前，做点什么
# # #         result = self.function(*args,**kwargs)
# # #         # 在调用函数之后，做点什么
# # #         # 并返回结果
# # #         return result
# # #
# # #
# # # # (3) 参数化装饰器
# # # # 在实际代码中通常需要使用参数化的装饰器。如果用函数作为装饰器的话，那么方法很简单:需要用到第二层包装。下面一个简单的装饰器示例，给定重复次数，
# # # # 每次被调用时都会重复执行一个装饰函数：
# # #
# # # def repeat(number=3):
# # #     '''
# # #     多次重复执行装饰函数
# # #     返回最后一次原始函数调用的值作为结果
# # #     :param number: 重复次数，默认是3
# # #     :return:
# # #     '''
# # #     def actual_dec(function):
# # #         def wrapper(*args,**kwargs):
# # #             result = None
# # #             for _ in range(number):
# # #                 result = function(*args,**kwargs)
# # #             return result
# # #         return wrapper
# # #     return actual_dec
# # # # 这样定义的装饰器可以接受参数
# # # #
# # # # @repeat(2)
# # # # def foo():
# # # #     print('asdfa~')
# # # # foo()
# # # #
# # # # print('~'*88)
# # # # @repeat()
# # # # def foo():
# # # #     print('888~')
# # # # foo()
# # # #
# # # # print('~'*88)
# # # # @repeat
# # # # def foo():
# # # #     print('888~')
# # # # foo()
# # #
# # #
# # # # 注意，即使参数化装饰器的参数有默认值，但是名字后面必须加括号。这是带默认参数的装饰器的正确用法
# # # # 没有加括号的话，在调用装饰函数时会出现错误
# # #
# # # # (4)  保存内省的装饰器
# # # # 使用装饰器的创建错误是在使用装饰器时不保存函数元数据(主要是文档字符串和原始函数名)。装饰器组合创建了一个新函数，并返回一个新对象，但是
# # # # 却完全没有考虑原始函数的标识。这将会使得调试这样装饰过的函数更加更加更加苦难，也会破坏可能用到的大多数自动生成文档的工具，
# # # # 因为无法访问原始的文档字符串和函数签名
# # # # 假设我们有一个虚设的(dummy)装饰器，仅有装饰作用，还有其他一些被装饰的函数：
# # # # 使用functools模块内置的wraps()装饰器 .这样定义的装饰器可以保存重要的函数元数据
# # #
# # #
# # # def dummy_dec(funtion):
# # #     @wraps(funtion)
# # #     def wrapped(*args,**kwargs):
# # #         '''包装函数内部文档。'''
# # #         return function(*args,**kwargs)
# # #     return wrapped
# # #
# # # @dummy_dec
# # # def func_wit():
# # #     '''这是我们想要的保存重要文档字符串'''
# # #
# # # print(func_wit.__name__)
# # # print(func_wit.__doc__)
# # #
# # # # 2.用法和有用的例子
# # # # 由于装饰器在模块被首次读取时由解释器来加载，所以它们的使用应受限于通用装饰器(wrapper)。如果装饰器与方法的类或所增强的函数签名绑定，那么
# # # # 应该将其重构为常规的可调用对象，以避免复杂性。在任何情况下，装饰器在处理api时，一个好的方法是将它们聚集在一个易于维护的模块中
# # #
# # # # 常见的装饰器模式：
# # # # 1. 参数检查   2. 缓存   3.代理 4.上下文提供者
# # #
# # # # (1)  参数检查
# # # # 检查函数接受或返回的参数，在特定上下文中执行时可能有用。举个例子，如果一个函数要通过xml-rpc来调用，那么python无法像静态语言那样直接提供
# # # # 其完整签名。当xml-rpc客户端请求函数签名时，就需要用这个功能提供内省能力
# # #
# # # # 自定义装饰器可以提供这种类型的签名，并确保输入和输出代表各自的签名参数。
# # # # 装饰器将函数注册到全局字典中，并将其参数和返回值保存在一个类型列表中。
# # #
# # # # (2) 缓存
# # # # 缓存装饰器与参数检查十分类似，不过它重点是关注那些内部状态不会影响输出的函数。每组参数都可以链接到唯一的结果。这种编程风格是函数式编程(functional programming)的特定，当输入值有限时可以使用
# # # # 因此，缓存装饰器可以将输出与计算它所需要的参数放在一起，并在后续的调用中直接返回它。这种行为被称为memoizing
# # #
# # #
# # # import time,hashlib,pickle
# # #
# # # cache = {}
# # #
# # # def is_obsolete(entry,duration):
# # #     return time.time() - entry['time'] > duration
# # #
# # # def compute_key(function,args,kw):
# # #     key = pickle.dumps((function.__name__,args,kw))
# # #     return hashlib.sha1(key).hexdigest()
# # #
# # # def memorize(duration=10):
# # #     def _memoize(function):
# # #         def __memoize(*args,**kw):
# # #             key = compute_key(function,args,kw)
# # #             # 是否已经拥有它了？
# # #             if (key in cache and
# # #             not is_obsolete(cache[key],duration)):
# # #                 print('we got a winner~~')
# # #                 return cache[key]['value']
# # #             # 计算
# # #             result = function(*args,**kw)
# # #             # 保存结果
# # #             cache[key] = {
# # #                 'value':result,
# # #                 'time':time.time()
# # #             }
# # #             return result
# # #         return __memoize
# # #     return _memoize
# # #
# # # # 利用已排序的参数值构建SHA哈希键，并将加过保存在一个全局字典中。利用pickle来建立hash,这是冻结所有作为参数传入的对象状态的快捷方式，
# # # # 以确保所有采纳数都满足要求
# # # # 缓存值还可以与函数本身绑定，以管理其作用域和生命周期，代替集中化的字典。但在任何情况下，更高效的装饰是会使用基于高级缓存算法的专用缓存库
# # # # （3） 代理
# # # # 代理装饰器使用全局机制来标记和注册函数。举个例子，一个根据当前用户来保护代码访问的安全层可以使用集中式检查器和相关的可调用对象要求的权限来实现
# # #
# # #
# # # class User(object):
# # #     def __init__(self,roles):
# # #         self.roles = roles
# # #
# # # class Unauthorized(Exception):
# # #     pass
# # #
# # # def protect(role):
# # #     def _protect(fuction):
# # #         def __protect(*args,**kwargs):
# # #             user = globals().get('user')
# # #             if user is None or role not in user.roles:
# # #                 raise Unauthorized("I won't tell you ")
# # #             return function(*args,**kwargs)
# # #         return __protect
# # #     return _protect
# # #
# # # # 这一模型常用于python web中，用于定义可发布类的安全性。例如，django提供装饰器来保护函数访问的安全
# # # #　下面一个示例，当前用户被保存在一个全局变量中。在方法被访问时装饰器会价差特尔角色
# # #
# # # tarek = User(('admin','user'))
# # # bill = User(('user',))
# # # class MySecrets(object):
# # #     @protect('admin')
# # #     def waffle_recipe(self):
# # #         print('use tons of butter~')
# # # print(88*'~')
# # # these_are = MySecrets()
# # # user = tarek
# # # print(these_are.waffle_recipe())
# # #
# # # # (4) 上下文提供者
# # # # 上下文装饰器确保函数可以运行在正确的上下文中，或在函数前后运行一些代码，它设定并复位一个特定的执行环境。举个例子，当一个数据项
# # # # 需要在多个线程之间共享时，就要用一个锁来保护它避免多次访问。这个锁可以在装饰器中编写
# # #
# # #
# # # from threading import RLock
# # # lock = RLock()
# # #
# # # def synchronized(function):
# # #     def _synchronized(*args,**kw):
# # #         lock.acquire()
# # #         try:
# # #             return function(*args,**kw)
# # #         finally:
# # #             lock.release()
# # #         return _synchronized
# # #
# # # @synchronized
# # # def thread_safe():  # 确保锁定资源
# # #     pass
# # # # 上下文装饰器通常会被上下文管理器(ｗith语句)替代，
# # #
# # #
# # # # ２．２．４　　上下文管理器————with语句
# # # # 为了确保即使在出现错误的勤快更新也能运行ｄｉａｍ，使用try...finanlly。　这一语句有很多使用场景　如下
# # # # １．关闭一个文件
# # # # ２．　释放一个锁
# # # # ３．　创建一个临时的代码补丁
# # # # ４．　在特殊环境中运行受保护的代码
# # # # with 语句为这些使用场景下的代码块包提供了一个简单的方法。即使该代码发生异常，也可以在其执行前后调用一些代码，例如，处理文件通用方式
# # #
# #
# # # hosts = open('/etc/hosts')
# # # try:
# # #     for line in hosts:
# # #         if line.startswith('#'):
# # #             continue
# # #         print(line.strip())
# # # finally:
# # #     hosts.close()
# #
# # # 上面的示例只针对linux系统，因为要读取位于etc文件加中的主机文件，但任何文本文件都可以用相同的方法来处理
# # # 利用with语句，重写上面代码
# #
# # with open('/etc/hosts') as hosts:
# #     for line in hosts:
# #         if line.startswith('#'):
# #             continue
# #         print(line.strip())
# #
# # # 在前面的示例中，open的作用是上下文管理器，确保即使出现异常也要在执行完for循环后关闭文件
# # # 与这条语句兼容的其他项目是来自threading模块的类
# #
# # # threading.Lock
# # # threading.RLock
# # # threading.Condition
# # # threading.Semaphore
# # # threading.BoundedSemapphore
# # # 一般语法和可能的实现
# # # with语句的一般语法的最简单形式如下：
# #
# # with context_manager:
# #     #代码块
# #      pass
# #
# # # 此外，如果上下文干力气听过了导航细纹变量，可以用as 子句来保存局部变量
# #
# # with context_manager as context:
# #     # 代码块
# #     pass
# #
# # # 注意，多个上下文管理器可以同时使用，如下
# #
# # with A() as a ,B() as b:
# #     pass
# #
# # # 上面的写法等价于嵌套使用，如下
# # with A() as a:
# #     with B() as b:
# #         pass
# #
# #
# # # (1)  作为一个类
# # # 任何实现了上下文管理器协议(context manager protocol) 的对象都可以用作上下文管理器。该协议包含两个特殊方法
# # # 1.  __enter__(self):
# # # 2.  __exit__(self,exc_type,exc_value,traceback)
# #
# # # 简而言之，执行with语句的过程如下：
# # # 1.调用__enter__方法。任何返回值都会绑定到指定的as子句
# # # 2. 执行内部代码块
# # # 3. 调用__exit__方法
# #
# # # __exit__接受代码快中二出现的是填入的3个参数。如果没有出现错误，那么这3个参数都被设为None,出现错误时，__exit__不应该重新引发这个错误
# # # ，因为这是调用者(caller)的责任。但它可以通过返回True来避免引发异常。这可用于实现一个特殊的场景
# # # 例如，contextmanager装饰器，但在大多数使用场景下，这一方法的正确行为是执行类似与finanlly子句的一些清理工作，无论代码块中发生了
# # # 什么，它都不会返回任何内容
# # # 下面是某个实现了这一协议的上线文管理器示例
#
# class ContextIllustration:
#     def __enter__(self):
#         print('entering context')
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('leaving context')
#         if exc_type is None:
#             print('with no error')
#         else:
#             print('with an error (%s)'% exc_val)
# #
# #
# # # 没有引发异常时的运行结果如下
# #
# # with ContextIllustration():
# #     print('inside')
#  #   引发异常时的输出如下
#
#  # with ContextIllustration():
#  #     raise RuntimeError('raised within "with"')
#  #  (2)  作为一个函数————contextlib模块
#
#
#  #  使用类似是实现Python语言提供的任何协议最灵活的方法。标准库中的contextlib模块，提供了与上下文管理器一起使用的辅助函数。它最有用
#  # 的部分是contextmanager装饰器。你可以在一个函数里面同时提供__enter__和__exit__两个部分，中间用yield语句分开(注意，这样函数就变成了生成器)
#  # 利用装饰器的例子如下
#
#
#  from contextlib import contextmanager
#
#  @contextmanager
#  def context_illustration():
#      print('entering context')
#      try:
#          yield
#      except Exception as e:
#          print('leaving context')
#          print('with an error (%s)'%e)
#          # 需要再次抛出异常
#          raise
#      else:
#          print('leaving contextx')
#          print('with no error')
#
# # 如果出现任何异常，该函数都需要再次抛出这个异常，以便传递它。注意，context_illustration在需要时可以有一些参数，只要在调用时提供这些参数即可
# # 这个小的辅助函数简化了常规的基于类的上下文api，正如生成器对基于类的迭代器api的作用一样。
# # 这个模块还提供了其他3个辅助函数
# # 1. closing(element):返回一个上下文管理器，在退出时会调用该元素的close方法。例如，它对处理流的类就很有用
# # 2. supress(*exceptions):它会压制发生在with语句正文中的特定异常。
# # 3.redirect_stdout(new_target)和 redirect_stderr(new_target):它会将的代码块内任何代码的sys.stdout或sys.stderr输出重定向
# # 到类文件(file-like)对象的另一个文件
#
# #