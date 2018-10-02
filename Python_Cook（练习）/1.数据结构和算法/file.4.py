#1.4 找到最大或最小的N个元素

#解决方案   heapq模块中有两个函数：nlargest(),nsmallest() 可以完成这个


# import heapq
#
# nums = [1,8,2,23,23,-4,9,4,42,32,2]
# print(heapq.nlargest(3,nums))
# print(heapq.nsmallest(3,nums))


#这两个函数都可以接收一个参数Key,从而允许他们工作在更加复杂的数据结构上，如
# import heapq
#
# profolio = [
#     {'name':'IBM','shares':100,'price':91.1},
#     {'name':'AAPL','shares':50,'price':543.22},
#     {'name':'FB','shares':200,'price':21.1},
#     {'name':'HPQ','shares':35,'price':31.11},
#     {'name':'YHOO','shares':45,'price':16.1},
#     {'name':'ACME','shares':75,'price':151.1},
#
# ]
#
# cheap = heapq.nsmallest(1,profolio,key=lambda s:s['price'])
#expen= heapq.nlargest(1,profolio,key=lambda s:s['price'])
# print(cheap)
# print('+'*88)
# print(expen)


#讨论   如果正在寻找最大或最小的N个元素，切且同集合 中的总数目相比，N很小，那么下面下面这些函数
# 可以提供更好的性能。这些函数首先会在底层将数据转化为列表，且元素会以堆的顺序排列


# nums = [1,8,2,23,23,-4,9,4,42,32,2]
# import heapq
# heap = list(nums)
# heapq.heapify(heap)
# print(heap)

#堆最重要的特性就是heap[0]总是最小的那个元素。此外,接下来的元素可依次通过heapq.heappop()轻松找到。
#该方法会将第一个元素（最小的）弹出。然后以第二小的元素取代之（这个操作的复杂度是O（logN），N代表堆的大小）。
#例如要找到第三小的水元素

# 当所要找的元素数量相对较小时，函数nlargest()和nsmallest()是最适用的。如果只是想找到最小和最大值（N=1时），
# 那么min(),max()是最快的。
# 如果N和集合大小差不多大时，通常更快的方法是先对集合排序，然后切片操作（如，使用sorted(items)[:N]或sorted(items)[-N:]）
#注意，nlargest(),nsmallest()的实际实现会根据它们的方式有所不同，可能会相应作出一些优化措施（比如，当N的大小同
# 输入大小很接近时，会采用排序的方法 ）
# 通常在优秀的算法和数据结构相关的书籍都能找到堆书籍结构的实现方法。在heapq模块的文档中实现了底层实现的细节。