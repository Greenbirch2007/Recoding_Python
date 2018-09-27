# 1.2从任意长度的可迭代对象中分解元素

# 问题  需要从某个可迭代对象中分解出N个元素，但是这个可迭代对象的长度可能超过N，
# 这会导致出现 “分解的值过多（too many values to unpack）”的异常


# 解决方案  Python的 "*表达式"可以用来解决这个问题
#比如计算平均成绩(去掉头尾)  这里表达式变成了一个列表

def drop_first_last(grades):
    first,*middle, last=grades
    return vars(middle)



record = ('Dave','dave@example.com','773-555-1212','847-555-1212')
name,email,*phone_numbers = record
print(name)
print(email)
print(phone_numbers)

#  由*修饰的变量也可以位于列表的第一个位置

# 讨论   对于分解未知或任意长度的可迭代对象，这种扩展的分解操作是量身定做的。通常
#这类可迭代对象中会有一些已知的组件或模式（例如，元素1之后的所有内容都是电话号码），利用*表达式分解
# 可迭代对象使得开发者能够轻松利用这些模式，而不必在可迭代对象中做复杂的的操作才能得到相关的元素。

# *式的语法在迭代一个变长的元组序列时很有用 如：
print(60*"+")
records = [('foo',1,2),
           ('bar','hello'),
           ('foo',3,4)]

def do_foo(x,y):
    print('foo',x,y)

def do_bar(s):
    print('bar',s)

for tag,*args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)


print(60*"+")

# 当和某些特定的字符串处理操作相结合，比如做拆分(splitting)操作时，这种*表达式的
# 语法所以支持的分解操作也非常有用

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname,*fields,homedir,sh = line.split(":")
print(uname)
print(fields)
print(homedir)
print(sh)

# 有时可能想分解出某些值后丢弃它们。在分解的时候，不能只是指定一个单独的*，但是
# 可以使用几个常用来表示待丢弃值的变量名，比如 _ 或ign(ignored)
print(60*"+")

record = ('ACME',50,123.45,(12,18,2012))
name,*_,(*_,year)= record
print(name)
print(year)


# *分解操作和各种函数式语言中的列表处理功能有类似，例如，如果有一个列表，可以向如下地下将其分解为头部和尾部
print(60*"+")

items = [1,10,7,4,5,9]
head,*tail = items
print(head)
print(tail)