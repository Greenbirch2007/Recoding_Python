# 5.2 高阶函数
# 接受函数为参数，或把函数作为结果返回的函数是高阶函数(higher-order function).map函数就是一个例子
# 内置sorted也是：可选的key参数用于提供一个函数，它会应用到各个元素上进行排序
# 示例5.3  根据单词长度给列表排序

fruits = ['strawberry','fig','apple','cherry','raspberry','banana']
print(sorted(fruits,key=len))

# 任何单参数函数都能作为key参数的值。

#　示例５．４　根据反向拼写给一个单词列表排序

def reverse(word):
    return word[::-1]         # 切片也能完成倒序操作

print(reverse('testing'))

print(sorted(fruits,key=reverse))


def factor(n):
    '''return n~~~~~~~~~'''
    return 1 if n < 2 else n* factor(n-1)

fact = factor
# 在函数式编程范式中，最常见的是map,filter,reduce。如果想使用不定量的参数调用函数，可以编写fn(*args,**keywords)

# map,filter,reduce的现代替代品
# python3中，列表推导式或生成器表达式具有了map和filter两个函数的功能

# 示例5.5   计算阶乘：map和filter与列表推导比较
print('~'*88)
print(list(map(fact,range(6))))
print([fact(n) for n in range(6)])
print('#'*88)
print(list(map(factor,filter(lambda n:n %2,range(6)))))
print([factor(n) for n in range(6) if n %2])

# 在Python3中，map和filer返回生成器(一种迭代器)，因此现在它们的直接替代品是生成器表达式(python2中，这两个函数返回列表，因此
# 最接近的替代品是列表推导)
# 在python2中，reduce是内置函数，但在python3中放到了functools模块里，这个函数最常用语求和。Python3中，最好使用sum函数

#　示例５．６＿　使用reduce和sum计算０－９９之和


from functools import reduce
from operator import add
print(reduce(add,range(100)))
print(sum(range(100)))

# sum和reduce的通用思想是把某个操作连续应用到序列的元素上，累计之前的结果，把一系列值归约成一个值
# all和any　约成一个值。
#all(iterable) 如果iterable的每个元素都是真值，返回True;all([]) 返回True
# any(iterable)  只要iterable中有元素是真值，就会返回True;any([])返回false;
