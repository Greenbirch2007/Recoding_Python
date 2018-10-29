# 1.20 将多个映射合并为单个映射

# 　１．２０．１　　问题

# 　我们有多个字典或映射，想在逻辑上将它们合并为一个单独的映射结果，以此执行某些特定的操作
# 　比如　查找值或检查键是否存在

# １．２０．２　　解决方案
# 　假设有两个字典

a = {'x':1,"z":3}
b = {'y':2,'z':4}

#  现在假设想执行查找操作，我们必须的检查这两个字典,一种简单的方法是利用collections模块中的ChainMap类来解决这个问题，例如

from collections import ChainMap

c = ChainMap(a,b)
# print(c['x']) # outputs 1 (from a)
# print(c['y'] # outputs 2 (from b)
# print(c['z'])         # outputs 3 (from a)

# 1.20.3 讨论
#  ChainMap 可接受多个映射然后在逻辑上它们表现为一个单独的映射结构。但是，这些映射在字面上并不会合并在一起。相反，ChainMap只是
# 简单的维护一个记录底层映射关系的列表。然后重定义常见的字典操作来扫描这个列表。大部分的操作都能正常工作，例如：
# print(len(c))
# print(list(c.keys()))
# print(list(c.values()))

#  如果有重复的键，那么这里会采用第一个映射所对应的值。因此，例子中的c['z']总是引用字典a中的值，而不是字典b中的值

# 修改映射的操作总是会作用在列出的第一个映射结构上。例如

# print(88*'@')
#
# c['z']= 10
# c['w'] = 66
# del c['x']
# print(a)
#
# del c['y']

# ChainMap　与带有作用域的值，比如编程语言中的变量(即全局变量，局部变量等)一起工作时特别有用。实际上这里
# 有一些方法使这个过程变得简单：
#
# values = ChainMap()
#
# values['x']=8
# # Add a new mapping
# print(values)
# values = values.new_child()
# values['x']= 6
# print(values)
# # Add a new mapping
# values = values.new_child()
# values['x'] =3
# print(values)
# print(values['x'])
#
# # discard last mapping
# values = values.parents
# print(values)


# 作为ChainMap的替代方案，我们可能会考虑利用字典的update()方法将多个　字典合并在一起。例如
# print(88*'@')
# merged = dict(b)
# merged.update(a)
# print(a)
# print(b)
# print(merged['x'])
# print(merged['y'])
# print(merged['z'])

# 这么做行得通，但这需要单独创建一个完整的字典对象(或修改其中现有的一个字典，这就破坏了原始数据)。此外，如果其中任何一个
# 原始字典做了修改，这个改变都不会反应到合并后的字典中。例如：
# print(88*'@')
#
# a['x'] = 13
# print(a)
# print(merged['x'])

# 而ChainMap使用的是原始的字典，因此它不会产生这种令人不悦的行为，例如

a = {'x':1,'z':3}
b = {'y':2,'z':6}

merged = ChainMap(a,b)
print(merged['x'])
print(merged['y'])
print(merged['z'])

a['x'] = 88
print(a)
print(a['x'])