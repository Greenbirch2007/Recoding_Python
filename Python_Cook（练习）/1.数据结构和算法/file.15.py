# 1.15 根据字段将记录分组

# １．１５．１　问题

# 　有一系列的字典或对象实例，我们想根据某个特定的字段（比如说日期）来分组迭代数据

# １．１５．２　解决方案

# itertools.groupby()函数在对数据进行分组时特别有用。如下：

rows = [
    {'address':'5451 N ckaare','date':'07/01/2012'},
    {'address':'1313 N ckaare','date':'07/06/2012'},
    {'address':'7914 a ckaare','date':'07/09/2012'},
    {'address':'7941 N ckaare','date':'07/11/2012'},
    {'address':'9741 N ckaare','date':'07/23/2012'},

]

# 现在假设根据日期以分组的方式迭代数据。要做到这些，首先以目标字段(在这个例子中是date)来对序列排序，然后再使用itertools.groupby()

from operator import itemgetter
from itertools import groupby

# Sort by the desired field first

rows.sort(key=itemgetter('address'))

# Iterate in groups

for date ,items in groupby(rows,key=itemgetter('date')):
    print(date)
    for i in items:
        print(" ",i)


# 1.15.3 讨论
# 函数groupby()通过扫描序列找出拥有相同值(或是由参数key指定的函数所返回的值)的序列项，并将它们分组。groupby()创建了一个迭代器，
# 而在每次迭代时都会返回一个值(value)和一个子迭代器(sub_iterator)，这个子迭代器可以产生所有在该分组内具有该值的项目

#　在这里重要的是首先要根据感兴趣的字段对数据进行排序。因为groupby()只能检查连续的项，不首先排序的话，将无法按所想的方式来对记录分组

# 如果只是简单地根据日期将数据分组到一起，放进一个大的数据结构中以允许进行随机访问，那么利用defaultdict()构建
#　一个一键多值字典(multidict)可能会更好　如下

from collections import defaultdict
rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)

# 这使得我们可以方便地访问每个日期的记录，如下：

for r in rows_by_date['07/01/2012']:
    print(r)


# 对于后面的这个例子，我们并不需要先对记录做排序。因此，如果不考虑内存方面的因素，这种
#　方式会比先排序再用groupby()迭代要来的更快。


