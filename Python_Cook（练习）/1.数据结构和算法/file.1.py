# 1.将序列分解为单独的变量(序列解包？)

# 问题 有一个包含N个元素的元组或序列，现在将将其分解为N个单独的变量


# 解决方案  (赋值------>分解)
# 任何序列（或可迭代的对象）都可以通过一个简单的赋值来分解为单独的变量
# 唯一的要求是变量的总数和结构要与序列相吻合，

# p = (4,5)
# x,y = p
# print(x)
# print(y)


data = ['ACME',50,91.1,(2012,12,21)]
name,shares,price,date = data

print(name)
print(shares)
print(price)
print(date)

# 如果元素的数量不匹配，将得到一个错误提示
# 讨论 实际上不仅仅只是元组或列表，只要对象恰好是可迭代的，那么就可以执行分解操作
# 这包括字符串，文件，迭代器以及生成器


s = 'Hello'
a,b,c,d,e = s
print(a)
print(b)
print(c)
print(d)
print(e)

print(30*'+')
# 当做分解操作时，有时候可能想丢弃某些特定的值。Python并没有提供特殊的语法来支持
# 实现这一点，但是通常可以选一个 使用 一个符号 来顶替需要丢弃的对象的位置
# 但是要确保选择的变量名没有在其他地方用到过。

__,shares,prices,_ =data

print(__)
print(shares)
print(prices)
print(_)