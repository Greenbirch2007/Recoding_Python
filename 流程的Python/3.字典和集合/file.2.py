# 3.2  字典推导


#  列表推导和生成器表达式的概念移植到了字典上,从而有了字典推导(还有集合推导),字典推导(dictcomp)可以从任何以键值对作为元素的可迭代对象中构建
#  出字典. 下面示例展示利用字典推导可以把一个装满元组的列表变成两个不同的字典

#  示例3-1   字典推导的应用


DIAL_CODES = [
    (86,'china'),
    (91,'india'),
    (88,'japan'),
]

c_code = {country:code for code,country in DIAL_CODES}
print(c_code)