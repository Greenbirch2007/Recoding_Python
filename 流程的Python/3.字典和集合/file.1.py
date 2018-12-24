# 第3章 字典和集合

#  本章内容如下

#  常见的字典方法
#  如何处理查找不到的键
#  标准库中dict类型的变种
#  set和frozenset类型
#  散列表的工作原理
#  散列表带来的潜在影响(什么样的数据类型可以作为键，不可预知的顺序，等等)

#  ３．１　泛映射类型 (掌握字典的构造)

a = dict(one=1,two=2,three=3)
print(a)
b = {'one':1,'two':2,'three':3}
print(b)
c = dict(zip(['one','two','three'],[1,2,3]))
print(c)
d = dict([('two',2),('one',1),('three',3)])
print(d)

e = dict({'three':3,'one':1,'two':2})
print(e)

#  字典推导(dict comprehension)也可以用来创建新的dict


