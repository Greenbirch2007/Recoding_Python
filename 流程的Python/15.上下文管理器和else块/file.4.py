#  15.4  使用@contextmanager

#  @contextmanager装饰器能减少创建上下问管理器的样板代码量,因为不用编写一个完整的类,定义__enter__和__exit__方法,而只需要实现有一个yield
#　语句的生成器，生成想让__enter__方法返回的值

# 在使用@contextmanager装饰的生成器中，yield语句额作用是把函数的定义体分为两部分：yield语句前面的所有代码在with块开始时，(即结合四起调用__enter__方法时)
# 执行，yield语句后面的代码在with块结束时(即调用__exit__方法时)执行

#  示例１５－５　　使用生成器实现的上下文管理器

# 示例１５－６　　测试looking_glass 上下文管理器函数

from mirror_gen import looking_glass

with looking_glass() as what:
    print('@@@``````')
    print(what)

print(what)

# contextlib.contextmanager装饰器会把函数包装成实现__enter__和__exit__方法的类

# 这个类的__enter__方法有如下作用：
#  1.  调用生成器函数，保存生成器对象(如gen)
#  2.　调用next(gen),执行到yield关键字所在的位置
#  ３．　返回next(gen)产出的值，以便把产出的值绑定到with/as　语句中的目标变量上

#  with块终止时，__exit__方法会做以下几件事：
#  如果在with块中抛出了异常，python解释器会将其捕获，然后在looking_glass函数的yield表达式里再次抛出．但是，那里没有处理错误的代码
#  因此looking_glass函数会中止，永远无法恢复原来的sys.stdout.write方法，异常系统处于无效状态

#  使用@contextmanager装饰器时，默认的行为是，装饰器提供的__exit__方法假定发给生成器的所有异常都得到处理了，因为应该压制异常．
#  如果不想让@contextmanager压制异常，必须在被装饰的函数中显示重新抛出异常
#  使用@contextmanager装饰器时，要把yield语句放在try/finanlly语句中(或放在with语句中)，这是无法避免的，因为我们永远不知道
# 上下文管理器的用户会在with块中做什么


# 生成器函数额作用更像协程:执行到某一点时暂停,让客户代码运行,知道客户让协程继续做事

#　@contextmanager装饰器有３个特性：１．函数装饰器，２．生成器　３．　with语句

