# 1.13 通过公共键对字典列表排序

# 1.13.1 问题
#　我们有一个字典列表，想根据一个或多个字典中的值来对列表排序


#　１．１３．２　解决方案

#　利用operator 模块中的itemgetter函数对这类结构进行排序是非常简单的。假设通过查询数据库项
# 　获取网站上的成员列表，我们得到了如下的数据结构

rows = [
    {'frame':'bian','lname':'jones','uid':1003},
    {'frame':'karson','lname':'belas','uid':1002},
    {'frame':'green','lname':'birch','uid':1001},
    {'frame':'big','lname':'lang','uid':1004}

]


#　根据所有的字典中共有的字段来对这些记录排序是非常简单的，如下


from operator import itemgetter

rows_by_fname = sorted(rows,key=itemgetter('frame'))
rows_by_uid = sorted(rows,key=itemgetter('uid'))

print(rows_by_fname)
print(88*'~')
print(rows_by_uid)

print(88*'~')


# itemgetter()函数还可以接受多个键。如下：

rows_by_lfname = sorted(rows,key=itemgetter('uid','lname'))
print(rows_by_lfname)

# 1.13.3 讨论

# 在这个例子中，rows被传递给内建的sorted()函数，该函数接受一个关键字参数key.这个参数应该代表一个可调用对象(callable)
# 该对象从rows中接受一个单独的元素作为输入并返回一个用来做排序依据的值。itemsgetter()函数创建的就是这样一个可调用对象


# 函数 operator.itemgetter()接受的参数可作为查询的标记，用来从rows的记录中提取出所需要的值。它可以是字典的键名称，
# 用数字表示的列表元素或是任何可以传给对象的__getitem__()方法的值。如果传多个标记给itemgetter(),那么它产生的
# 可调用对象将返回一个包含所有元素在内的元组，然后sorted()将根据对元组的排序结果来排序输出结果。如果想同时针对多个
# 字段做排序(比如例子中的姓和名),那么这是非常有用的

# rows_by_fname = sorted(rows,key=lambda r:r['frame'])
# print(88*'=|=')
# print(rows_by_fname)
# print(88*'=|=')
# rows_by_lfname = sorted(rows,key=lambda r:r['lfname'])
# print(rows_by_lfname)

# 这种解决方案通常也能正常工作，但是用itemgetter()通常会运行得更快一些。因此如果需要考虑性能问题的话，应该是用itemgetter()

# 最后需要忘了本节中所展示的技术同样适用于min(),max()这样的函数

min_row = min(rows,key=itemgetter('uid'))
print(min_row)

print(88*'^')

max_row = max(rows,key=itemgetter('uid'))
print(max_row)