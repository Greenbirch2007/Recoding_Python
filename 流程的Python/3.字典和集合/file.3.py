#  3.3  常见的映射方法

#  有三种    dict    collections.defaultdict,        collections.OrderedDict



#   用setfault处理找不到的键


#  当字典d[k]不能找到正确的键的时候.Python会抛出异常


#  那么,在单纯地查找取值(而不是通过查找来插入新值)的时候,该怎么处理找不到的键呢?