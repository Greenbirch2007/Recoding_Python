#  3.8集合论


#  集合的本质是许多唯一对象的聚集，因此，集合可以用于去重


#  集合中的元素必须是可散列的，set类型本身是不可散列的，但是frozenset可以．因此可以创建一个包含不同frozenset的set



#  3.8.1  集合字面量

#  除了空集外，集合的字面量－－－{1},{1,2}，如果是空集，那么必须写成set()的形式

#  在python3中，除了空集，集合的字符串表示形式总是以{...}的形式出现

s = {1}
print(type(s))
print(s)
s.pop()
print(s)


#  3.8.2  集合推导

#  python2.7带来了集合推导(setcomps)

#  示例３－１３　　　新建一个字符集合，该集合里的每个字符

from unicodedata import name
print({chr(i) for i in range(32,256) if 'SIGN' in name(chr(i),'')})


#  3.8.3 　集合的操作

#  集合的数学运算，这些方法或会生成新集合，或会在条件允许的情况下就地修改集合

#  集合的比较运算符，返回值是布尔类型

#  集合类型的其他方法


#  s.add(e)    把元素e添加到s中
#  s.clear()  移除掉s中的所有元素
#  s.copy()   对s浅复制
#  s.discard(e)   如果s里有e这个元素的话，把它移除
#  s.__iter__()   返回s的迭代器
#  s.__len__()   len(s)
#  s.pop()  从s中移除一个元素并返回它的值，若s为空，则抛出KeyError异常
#  s.remove(e)   从s中移除e元素，若e元素不存在，则抛出KeyError异常


