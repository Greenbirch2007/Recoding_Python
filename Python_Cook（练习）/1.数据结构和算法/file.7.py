# 1.7 让字典保持有序

# 1.7.1  问题  我们想创建一个字典，同时当对字典做迭代或序列化操作时，也能控制其中元素的顺序

# 1.7.2 解决方案 要控制字典中元素的顺序，可以使用collections模块中的OrderedDict类。 当对字典
#做迭代时，它会严格按照元素初始添加的顺序进行　如


from collections import OrderedDict

d = OrderedDict()

d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
d['karson'] = 5
d['Greenbirch'] = 6

# Outputs "foo 1",...

for key in d:
    print(key,d[key])

print(88*'~')

# 当想构建一个映射结构以便稍后对其做序列化或编码成另一个格式时，OrderedDict就显得很有用。
# 例如，如果想进行JSON编码时精确控制各字段的顺序，那么只要首先在OrderedDict中构建数据就可以了

import json
print(json.dumps(d))

print(88*'~')


# 1.7.3 讨论　OrderedDict 内部维护了一个双向链表，它会根据元素加入的顺序来排列键的位置。
# 第一个新加入的元素被放置在链表的末尾。接下来对已存在的键做重新赋值不会改变键的顺序
# 请注意OrderedDict的大小是普通字典的２倍多，这是由于它额外创建的链表所致。因此，如果打算
# 构建一个涉及大量　OrderedDict实例的数据结构（例如从CSV文件中读取100000行内容到OrderedDict列表中）。
#那么需要认真对应用做需求分析，从而判断使用　OrderedDict　所带来的好处是否能够超越因额外的
# 内存开销所带来的缺点

