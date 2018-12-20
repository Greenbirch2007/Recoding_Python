#　２．７　list.sort方法和内置函数sorted


#　list.sort方法会就地排序列表，也就是说不会把原列表复制一份．这也是这个方法的返回值是None的原因．
#　如果一个函数或方法对对象进行的是就地改动，那它就应该返回None,好让调用者知道传入的参数发生了变动，而且并为产生新的对象，例如random,shuffle函数

#　与list.sort相反的内置函数sorted，它会新建一个列表作为返回值．这个方法可以接受任何形式的可迭代对象作为参数，甚至包括不可变序列或生成器．
#　而不管sorted接受的是怎样的参数，它最后都会返回一个列表

#　不管是list.sort方法还是sorted函数，都有两个可选的关键字参数
#　reversed
#　如果被设定为True,被排序的序列里的元素会以降序输出(也就是说把最大值当做最小值来排序)这个参数的默认值是False
#　key
#　一个只有一个参数的函数，这个函数会被用在序列里的每一个元素上，所产生的结果将是排序算法依赖的对比关键字
#　参数的默认值是恒等函数(identify function),也就是默认用元素自己的值来排序


#　可选参数key还可以在内置函数min(),max()中起作用．另外，还有些标准库的函数也接受这个参数，如itertools.groupby(), heapq.nlargest()


fruits = ['grape','raspberry','apple','banana']

print(sorted(fruits))

print(sorted(fruits,reverse=True))

print(sorted(fruits,key=len))
# 已经排序的序列还可以用来进行快速搜索，而标准库的bisect模块给我提供了二分查找算法，