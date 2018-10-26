# 1.11  对切片命名

#1.11.1 问题

# 我们的代码已经变得无法阅读，到处都是硬编码的切片索引，我们想将它们清理干净

# 1.11.2 解决方案
#　假设有一些代码用来从字符串的固定位置中取出具体的数据（比如从一个平面文件或类似的格式）：
#　平面文件（flat file)是一种包含没有相对关系结构的记录文件、

#　为什么不对切片命名？

#1.11.3 讨论

#　作为一条基本准则，代码中如果有很多硬编码的索引值，将导致可读性和可维护性都不好。
#　一般来说，内置的slice()函数会创建一个切片对象，可以用在任何允许进行切片操作的地方

# items = [0,1,2,3,4,5,6]
# a = slice(2,4)
# print(items[2:4])
# print(items[a])
# items[a] = [10,11]
# print(items)
#
# print(88*"~")
#
# del items[a]
#
# print(88*"~")
# print(items)

# 如果有一个slice 对象的实例s，可以分别通过   s.start,s.stop以及s.step属性来得到关于该对象的信息


# a = slice
# print(a.start)

# 此外，可以通过使用indices(size) 方法将切片映射到特定大小的序列上，这会返回一个(start,stop,step)元组，
#　所有的值都已经恰当地限制在边界以内（当做索引操作时可避免出现IndexError异常）例如：
a = slice(3)

s = "HelloWorld"
print(a.indices(len(s)))

for i in range(*a.indices(len(s))):
    print(s[i])