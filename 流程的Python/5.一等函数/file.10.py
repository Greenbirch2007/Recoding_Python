# # # 5.10 支持函数式编程的包
# #
# # # 得益于operator和functools等包的支持，函数式编程风格可以信手拈来
# #
# # # 5.10.1 operator模块
# #
# # # 在函数式编程中，经常需要把算数运算符当做函数使用。例如，如何使用lambda表达式
# # # 示例５．２１　　　使用reduce函数和一个匿名函数计算阶乘
# #
# #
# # from functools import reduce
# #
# # def fact(n):
# #     return reduce(lambda a,b:a*b,range(1,n+1))
# #
# # # operator模块为多个算术运算符提供相应的函数，从而避免编写lambda a,b:a*b这种平凡的匿名函数。使用算术运算符函数，如下
# # # 示例５．２２　　使用reduce和operator.mul 函数计算阶乘
# #
# #
# #
# # from functools import reduce
# # from operator import mul
# #
# # def fact1(n):
# #     return reduce(mul,range(1,n+1))
# #
# #
# # # operator模块中还有一类函数，能替代从序列中取出元素或读取对象属性的lambda表达式：因此，itemgetter和attrgetter其实会自行构建函数
# # # itemgetter的常见用途：根据元组的某个字段给元组列表排序。itemgetter(1)的作用与lambda fields:fields[1]一样：创建一个接受集合的函数，返回索引位1上的元素
# #
# # # 示例5.23  演示使用itemgetter排序一个元组列表
#
# metro_data = [
#     ('Tokyo','JP',36.933,(35.689,139.46464)),
#     ('Delhi NCR','IN',21.464,(28.61,71.144)),
#     ('Mexico City','MX',20.146,(19.141,-99.13))]
#
# #
# # from operator import itemgetter
# #
# # for city in sorted(metro_data,key=itemgetter(2)):
# #     print(city)
# #
# # # 如果把多个参数传给itemgetter,它构建的函数会返回提取的值构成的元组：
# #
# # cc_name = itemgetter(1,0)
# # for city in metro_data:
# #     print(cc_name(city))
# #
# # # itemgetter使用[]运算符，因此它不仅支持序列，还支持映射和其他实现__getitem__方法的类
# # # attrgetter与itemgetter作用类似，它创建的函数根据名称提取对象的属性。如果把多个属性名传给attrgetter,它也会返回提取
# # # 的值构成的元组。此外，如果参数名中包含.(点号)，attrgetter会深入嵌套对象，获取指定的属性。这些行为如下面实例，
# # # 这个控制台会话不断，因为我们要构建一个嵌套结构，这样才能展示attrgetter如何处理包含点号的属性名
# #
# # # 示例5.24  定义一个namedtuple,名为metra_data，使用attrgetter处理它
#
# from collections import namedtuple
#
# LatLong = namedtuple('LatLong','lat long')
# Metropolis = namedtuple('Metropolis','name cc pop coord')
# metro_areas = [Metropolis(name,cc,pop,LatLong(lat,long)) for name,cc,pop,(lat,long) in metro_data]
#
# print(metro_areas[0])
# print(metro_areas[0].coord)
#
#
# print('~'*88)
#
# from operator import attrgetter
#
# name_lat = attrgetter('name','coord.lat')
# print(name_lat)
#
# for city in sorted(metro_areas,key=attrgetter('coord.lat')):
#     print(name_lat(city))
#
#
# # 下面是operator模块中定义的部分函数(省略了以_开头的名称，因为它们基本上是实现细节)：
# # 在operator模块有一个methodcaller函数，它的作用与attrgetter和itemgetter类似，它会自行创建函数。methodcaller创建的函数
# # 会在对象上调用参数指定的方法，如下
#
# #示例　５．２５　　　methodcaller使用示例：第二个测试展示绑定额外参数的方式
#
# from operator import methodcaller
#
# s = 'The time has come'
# upcase = methodcaller('upper')
# print(upcase(s))
#
# hiphenate = methodcaller('replace',' ','-')
# print(hiphenate(s))
#
# # 示例５．２５中的第一个测试只是为了展示methodcaller的用法，如果想把str,upper作为函数使用，只需在str类上调用，并传入一个字符串参数。如下
#
# str.upper(s)
#
# # 示例５．２５中的第二个测试表明，methodcaller还可以冻结某些参数，也就是部分应用(pattial application),这与functools.partial函数的作用类似
#
# # 5.10.2   使用functools.partial冻结参数
#
# #  functools模块提供了一系列高阶函数，如reduce.剩下的函数，常用的有partial,partialmethod
#
# #  functools.partial这个高阶函数用于部分应用一个函数。部分应用是指，基于一个函数创建一个新的可调用对象，把原函数的某些参数固定。使用这个
# #  函数可以把接受一个或多个参数的函数改编成需要回调的api,这样参数更少
# #  示例5.26  使用partial 把一个两参数函数改编成需要单参数和可调用对象
# print('#'*88)
#
# from operator import mul
# from functools import partial
# triple = partial(mul,3)
# print(triple(8))
# print(list(map(triple,range(1,10))))
#
# # 如果处理多国语言编写的文本，在比较或排序之前可能会想使用unicode.normalize('NFC',s)处理所有字符串s，如果经常真没做，可以定义一个nfc函数。
#
# #  示例5.27  使用partial构建一个遍历的Unicode规范化函数
#
# import unicodedata,functools
# nfc = functools.partial(unicodedata.normalize,'NFC')
# s1 = 'cafe'
# s2 = 'cafe/u001'
# print(s1,s2)
# print(nfc(s1),nfc(s2))
# # partial 的第一个参数是一个可调用对象，后面跟着任意个要绑定的定位参数和关键字参数，
# #　示例５．２８　　定义的tag函数上使用partial,冻结一个定位参数和一个关键字参数
#
# #  示例５．２８　　把partial应用到示例５．１０　中定义的tag函数上
#
from tag import tag

print(tag)
from functools import partial
pic = partial(tag,'img',cls='pic-frame')
print(pic(src='wumpus.jpeg'))
print(pic)
print(pic.func)
print(pic.args)
print(pic.keywords)

# partial()返回一个functools.partial对象
#　functools.partial对象提供了访问原函数和固定参数的属性

# functools.partialmethodhansh 的函数的作用与partial一样，不过是用于处理方法的

# functools模块中的lru_cache函数，它会做备忘(memoization),这是一种自动化措施，它会存储耗时的函数调用结果，避免重新计算
