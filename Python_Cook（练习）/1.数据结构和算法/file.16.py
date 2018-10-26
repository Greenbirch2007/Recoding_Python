#　１．１６　筛选序列中的元素

#　１．１６．１　问题

#　　序列中含有一些数据，我们需要提取出其中的值或根据某些标准对序列做删减

#　１．１６．２　解决方案
#　要筛选序列中的数据，通常最简单的方式是使用列表推导式(list comprehension) .例如：

# mylist = [1,4,-5,10,-7,2,3,-1]

# a1 = [n for n in mylist if n>0]
# print(a1)
# a2 = [n for n in mylist if n<0]
# print(a2)
#
#
# print(88*'%')

# 使用列表推导式的一个潜在缺点是如果原始输入非常大的话，这么做可能会产生一个庞大的结果。如果这是你需要考虑的问题，那么可以
#　使用生成器表达式通过迭代的方式产生筛选的结果　　如下：


# pos = (n for n in mylist if n>0)
# print(pos)
# for x in pos:
#     print(x)


# 有时候筛选的标准没法简单地表示在列表推导式或生成器表达式中。比如，假设筛选过程涉及异常处理或其他一些
#　复杂的细节。基于此，可以将处理筛选逻辑的代码放到单独的函数中，然后使用呢间的filter()函数处理，　如下

# values = ['1','2','-3','-','4','N/A','5']
#
# def is_int(val):
#     try:
#         x = int(val)
#         return True
#     except ValueError:
#         return False
#
# ivals = list(filter(is_int,values))
# print(ivals)

# filter()创建了一个迭代器，因此如果我们想要的是列表形式的结果，请确保加上了list()

#  1.16.3讨论
# 　列表推导式和生成器表达式通常是用来筛选数据的最简单和最直接的方式。此外，它们还具有同事对数据做转换的能力

# mylist = [1,4,-5,10,-7,2,3,-1]
#
# import math
#
# sqrt_list = [math.sqrt(n) for n in mylist if n>0]
# print(sqrt_list)

# 关于筛选数据，有一种情况是用新值替换掉不满足标准的值，而不是丢弃它们。例如，除了要找到正整数职位，我们也许还希望在指定
# 的范围内将不满足要求的值替换掉。通常，这可以通过将筛选条件移到一个条件表达式中来轻松实现，如下：

# clip_neg = [n if n > 0 else 0 for n in mylist]
# print(clip_neg)
#
# clip_pos = [n if n < 0 else 0 for n in mylist]
# print(clip_pos)

# 另一个值得一提的筛选工具是　itertools.compress(),它接受一个可迭代对象以及一个布尔选择器序列作为输入。
# 　输出时，它会给出所有在相应的布尔选择器中为true的可迭代对象元素。如果向把对一个序列的筛选结果施加到
# 　另一个相关的序列上，这很有用。如，假设有下面两列数据


addresses = [
    '5412 N claer',
    '5353 N claer',
    '3453 N claer',
    '15765 N claer'

]

counts = [0,3,10,4,1,7,6,1]

# 现在我们想构建一个地址列表，其中相应的count值要大于５，可像如下操作：

from itertools import compress

more5 = [n > 5 for n in counts]
print(more5)
print(list(compress(addresses,more5))) # 使用了索引值

# 这里的关键在于首先创建一个布尔序列，用来表示哪个元素可满足我们的条件。然后compress()函数
# 挑选出满足布尔值为true的相应元素

# 同filter()函数一样，正常情况下compress()会返回一个迭代器。因此，如果需要的话，
# 得使用list()将结果转换为列表