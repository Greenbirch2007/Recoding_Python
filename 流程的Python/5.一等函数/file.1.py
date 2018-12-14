# 第５章　　一等函数

# 在python中，函数是一等对象。一等对象需要满足的条件：
# １．在运行时创建
# ２．　能赋值给变量或数据结构中的元素
# ３．　能作为参数传递给函数
# ４．　能作为函数的返回结果

# 在python中，整数，字符串和字典都死一等对象
# ５．１　　把函数视作对象
# 这里创建一个函数，然后调用它，读取它的__doc__属性，并且确定函数对象本身是function类的实例

# 示例５．１　　创建并测试一个函数，然后读取它的的__doc__属性，再检查它的类型


def factor(n):
    '''return n~~~~~~~~~'''
    return 1 if n < 2 else n* factor(n-1)


# print(factor(6))
# print(factor.__doc__)
# print(type(factor))

#__doc__属性用于生成对象的帮助文本。在python交互控制台中，
# print(help(factor)
# map函数返回一个可迭代对象，里面额元素是把第一个参数(一个函数)应用到第二个参数(一个可迭代对象，这里是range(11))中各个元素上得到结果

# 示例５．２　　通过别的名称使用函数，再把函数作为参数传递

fact = factor

print(fact)
print(fact(6))
print(map(factor,range(6)))
print(list(map(factor,range(6))))

# 有了一等函数，就可以使用函数式风格编程。可以使用高阶函数