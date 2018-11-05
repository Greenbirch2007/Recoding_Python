# ７．４　从函数中返回多个值

# ７．４．１　问题
# 我们向从函数中返回多个值

# ７．４．２　解决方案
# 要从函数中返回多个值，只要简单地返回一个元组即可，如下

def myfun():
    return 1,2,3


t =myfun()
a,b,c = myfun()

print(t)
print(a)
print(b)
print(c)

# 7.4.3 讨论
# 尽管看起来myFun()返回了多个值，但实际上它只创造了一个元组而已。这看起来有点奇怪，但是实际上元组是通过逗号来组成的，恶如不是圆括号

# with parentheses

a = (1,2)
print(a)

# without parenteses

b = 1,3
print(b)


# 当调用的函数返回了元组，通常会将结果赋值给多个变量，就像示例中那样。实际上这就是简单的元组解包。
# 返回的值也可以只赋给一个单独的变量：
x = myfun()
print(x)
# x就代表整个元组