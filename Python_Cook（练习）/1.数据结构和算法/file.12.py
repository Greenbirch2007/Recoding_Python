# 1.12 找出序列中出现次数最多的元素

# １．１２．１　问题　

#　我们有一个元素序列，想知道在序列中出现次数最多的元素是什么

# 1.12.2 解决方案

#　collections 模块中的Counte类正是为此类问题所设计的。它甚至有一个非常方便的most_common()方法可以直接告诉我们答案
#　为了说明用法，假设有一个列表，列表中是一系列的单词，我们想找出哪些单词出现的最频繁，如下

words = ['look','into','my','eyes','look','into','my','eyes',
         'the','eyes','the','eyes','the','eyes','not','around','the',
         'eyes',"don't",'look','around','the','eyes','look','into',
         'my','eyes','under']


from collections import Counter

word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)

# 1.12.3 讨论
# 　可以给Counter对象提供任何可哈希的对象序列作为输入。在底层实现中，Counter是一个字典，
# 　在元素和它们出现的次数间做了映射　　例如：

print(88*'~')

print(word_counts['not'])
print(word_counts['eyes'])


#  如果向手动增加计数，只需简单地自增即可

morewords = ['why','are','you','not','looking','in','my','eyes']
for word in morewords:
    word_counts[word] += 1

print(word_counts['eyes'])

# 另一种方式是使用update()方法

print(88*'~')

print(word_counts.update(morewords))

#　关于Counter对象有一个不为人知的特性，那就是它们可以轻松地同各种数学运算操作结合起来使用。例如：

print(88*'~')

a = Counter(words)
b = Counter(morewords)
print(88*'~')
print(a)
print(88*'~')
print(b)


# Combine counts　连接计数(加法)

c = a + b
print(88*'~')
print(c)


# subtract counts 　减法
print(88*'~')

d = a - b
print(d)

#　不用说，当面对任何需要对数据制表或计数的问题时，Counter对象都是你手边得力工具
# 比起利用字典自己手写算法，更应该采用这种方式完成任务