# 1.6 在字典中将键映射到多个值上

# 1.6.1 问题  我们想要一个能将键（key） 映射到多个值的字典（即所谓的一键多值字典[multidict]）


# 1.6.2 解决方案  字典是一种关联容器，每个键都映射到一个端度的值上。如果想让键映射到多个值
# 需要将这多个值保存到另一个容器如列表或集合中。 如下

d = {
    'a':[1,2,3],
    'b':[4,5]
}

e = {
    'a':{1,2,3},
    'b':{4,5}
}

# 要使用列表还是集合安全取决于应用的企图。如果希望保留元素插入的顺序，就用列表。
# 如果希望消除重复元素（且不在意他们的顺序）。就用集合。

# 为了能方便地创建这样的字典，可以利用collections模块中的defaultdict类。defaultdict的一个特点
# 就是它自动初始化第一个值，这样只需要关注添加元素即可 如：

from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['a'].append(3)
d['a'].append(4)
d['a'].append(5)
d['a'].append(6)

print(d)
print(88*'~')

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(1)
d['b'].add(2)
print(d)
print(88*'~')


# 关于 defaultdict,需要注意的一个地方是，它会自动创建字典表项以待稍后的访问（即使
# 这些表项当前咋字典中还没有找到）。如果不需要这个功能，可以在普通的字典上滴啊用setdefault()方法来取代， 如


d = {} # A regular dictionary

d.setdefault('a',{}).append(1)
d.setdefault('a',{}).append(2)
d.setdefault('b',[]).append(2)
print(d)
print(88*'~')

# 然而，许多程序员觉得使用setdefault()有些不自然，更别提每次调用它时都会创建一个
# 初始值的新实例了（例子中的空列表[]）


#1.6.3 讨论 原则上，构建一个一键多值字典是很容易分。但是如果试着自己对第一个值做初始化操作，
# 这就会变得很杂乱，例如，如下

d = {}
for key,value in paris:
    if key not in d:
        d[key]= []
    d[key].append(value)

# 使用defaultdict后代码就清晰很多“
d = defaultdict(list)
for key,value in paris:
    d[key].append(value)

# 这一节的内容同数据处理中的记录归组问题有很强的关联
