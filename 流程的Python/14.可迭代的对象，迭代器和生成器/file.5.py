# #  14.10   python3.3  中新出现的句法:yield from
#
#
# # 如果生成器函数需要产出另一个生成器的值,传统的解决方法是使用嵌套的for循环.
# # 下面就实现一个chain生成器
#
# def chain(*iterables):
#     for it in iterables:
#         for i in it:
#             yield i
#
#
# s = 'ABC'
# t = tuple(range(3))
# print(t)
# print(list(chain(s,t)))
#
#
# # 标准库中的itertools.chain函数使用C语言编写的，chain生成器函数把操作依次交给接收到的各个可迭代对象处理　
#
# print(88*'~')
#
# def chain(*iterables):
#     for i in iterables:
#         yield from i
#
# print(list(chain(s,t)))
#
# # 可以看出，yield from i 完全代替了内层的for循环．在这个示例中使用yield from 是对的，而且代码读起来更顺畅，不过感觉更像语法糖．除了
# #  代替循环之外，yield from 还会创建通道，把内层生成器直接与外层生成器的客户端联系起来．把生成器当成协程使用时，这个通道特别重要
# #  不仅能为客户端代码生成值，还能使用客户端提供的值．
#
# #  １４．１１　　可迭代的归约函数
# #  下面的函数都接受一个可迭代的对象，然后返回单个结果，这些函数叫"归约"函数，"合拢"函数或"累加"函数，这里列出的每个内置函数都可以使用
# #  functools.reduce函数实现，内置是因为使用它们便于解决常见的问题．此外，对all和any函数来说，有一项重要的优化措施是reduce函数做不到：
# #  这两个函数会短路(即一旦确定了结果就立即停止使用迭代器)
#
# #  表１４－６　　读取迭代器，返回单个值的内置函数
#
# #  all(),any() ,max(), min(), functools.reduce   sum()
#
#
# #  示例１４－２３　　把几个序列传给all和any函数后得到的结果
#
# print(all([1,2,3]))
# print(all([1,0,3]))
# print(all([]))
# print(any([1,2,3]))
# print(any([1,0,3]))
# print(any([0,0,0]))
# print(any([]))

g = (n for n in [0,0,0,7,8])
print(any(g))
print(next(g))
# 还有一个内置的函数接受一个可迭代的对象，返回不同的值－－sorted．reversed是生成器函数，与此不同　，sorted会构建并返回真正的列表．毕竟
#  要读取输入的可迭代对象中的每一个元素才能排序,而且排序的对象是列表,因为sorted操作完成后返回排序后的列表.我在这里提到sorted,是因为
#  它可以处理任意的可迭代对象.
#  当然,sorted和这些归约函数只能处理最终会停止的可迭代对象.否则,这些函数会一直收集元素,永远无法返回结果


#  14.12  深入分析 iter函数

#  在python中迭代对象x时会调用iter(x)
#  可是,iter函数还有一个用法:传入两个参数,使用常规的函数或任何可调用的对象创建迭代器.这样使用时,第一个参数必须是可调用的对象,用于不断调用(没有参数)
#  产出各个值;第二个值是哨符,这是个标记值,当可调用的对象返回这个值时,触发迭代器抛出StopIteration异常,而不产出哨符


from random import randint


def d6():
    return randint(1,6)


d6_iter = iter(d6,1)
print(d6_iter)


for roll in d6_iter:
    print(roll)


#  这里的iter函数返回一个callable_iterable对象.示例中的for循环可能运行特别长的时间,不过肯定不会打印1,因为1是哨符.与常规的迭代器一样,
# 这个示例中的d6_iter对象一旦耗尽就没用了.如果想重新开始,必须再次调用iter(...),重新构建迭代器

#  内置函数iter的文档中有个使用的例子,这段代码逐行读取文件,直到遇到空行或到达文件末尾为止:

with open('mydata.txt') as fp:
    for line in iter(fp.readable,'\n'):
        process_line(line)

# 最后一个例子,在说明如何使用生成器高效处理大量数据

#