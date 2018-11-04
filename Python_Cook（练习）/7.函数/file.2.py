# 7.2 编写只接受关键字参数的函数
# ７．２．１　问题
# 我们希望函数只通过关键字的形式接受特定的参数.
# 7.2.2 解决方案
# 如果将关键字参数放置在以*开头或是一个单独的*之后，这个特性就很容易实现。示例如下：

def recv(maxsie,*,block):
    'receives a message'
    pass

print(recv(1024,block=True))

# 这项技术也可以用来为那些可接受任意数量的位置参数的函数来指定关键字阐述，示例如下：

def minium(*values,clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m

print(minium(1,5,7,-6,1,0))
print(minium(1,5,7,-6,1,clip=0))

# 7.2.3 讨论
# ７．２．３　讨论当制定可选的函数参数时，keyword-only参数常常是一种提高代码可读性的好方法。
# 比如，考虑下面的调用
#
# msg = recv(1024,False)
# print(msg)
#

# 如果某些人不熟悉recv()的工作方式，他们可能会搞不清楚这里的False参数到底表示了什么意义。而另一方面，
# 如果这个调用可以写成下面这样的话，那就显得清晰多了

msg = recv(1024,block=False)
print(msg)

# 在有关**kwargs的技巧中，使用keyword-only参数常常也是可取的，因为当用户求帮助信息时，它们可以适时的显示出来

print(help(recv))

# keyword-only 参数在更加高级的上下文环境中同样能起到作用。比如说，可以用来为函数注入参数，这些函数利用
# *args ,**kwargs接受所有的输入参数。