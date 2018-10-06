# 1.10 从序列中移除重复项且保持元素间顺序不变

# 1.10.1 问题  我们想去除序列中的重复元素，但仍然保持剩下的元素顺序不变


# 1.10.2 解决方案
#  可哈希的：如果一个对象是可哈希的，那么在它的生存期内必须是不可变的，它需要有一个__hash__()方法
#  整数，浮点数，字符串，元组都是不可变的
# 如果序列中的值是可哈希的，那么这个问题可以通过使用集合和生成器轻松解决。如下：

# def dedupe(items):
#     seen = set()
#     for item in items:
#         if item not in seen:
#             yield item
#             seen.add(item)
#
# a = [1,5,2,1,3,6,7,61,3,3,1,3,8]
#
# t = list(dedupe(a))
# print(t)

#  只有当序列中的元素是可哈希的时候才能这么做。如果想在不可哈希的对象（比如列表）
# 序列中去除重复项，需要对以上代码做一个修改：

def dedupe(items,key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)  # 保证取到不可变的元素
        if val not in seen:
            yield item
            seen.add(val)

#  这里参数key 的作用是指定一个函数用来将序列中的元素转换为不可哈希的类型，这么做的
# 目的是为了检车重复项，如下：

a = [{'x':1,'y':2},{'x':1,'y':3},{'x':1,'y':2},{'x':2,'y':4}]
t = list(dedupe(a, key=lambda d: (d['x'],d['y'])))
print(t)
t = list(dedupe(a,key= lambda d: d['x']))
print(t)

# 如果希望在一个较复杂的数据结构中，只根据对象的某个字段或属性来去除重复项，那么
# 后一种积极方案同样完美

# 1.10.3 讨论
# 如果想要做的只是去除重复项，那么通常足够简单的办法就是构建一个集合。如下：
# 注意集合无法对字典去重！
print(88*'~')

a = [1,5,2,1,3,6,7,61,3,3,1,3,8]
print(set(a))

# 但是这种方法不能保证元素间的顺序不变，得到的结果被打乱， 前面的解决方案更优

# 本节 对生成器的使用反映出一个试试，就是我们可能会希望这个函数尽可能通用——不必绑定
# 在只能对列表进行处理，比如，如果想读取一个文件，去除其中重复的文本行，可以只需要这样处理：

with open(somefile,'r') as f:
    for line in dedupe(f):
        pass

# 我们的dedupe函数也模仿了内置函数 sorted(),min()以及max()对key函数的使用方式。