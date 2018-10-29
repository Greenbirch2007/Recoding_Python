# 1.19 同时对数据做转换和换算

# 1.19.1 问题
#　我们需要调用一个换算(reducton) 函数（例如，sum(),min(),max()）,但首先得对数据做转换或筛选

#　1.19.2 解决方案

#　有一种非常优雅的方式能将数据换算和转换结合在一起————在函数参数中使用生成器表达式。
#　例如，如果想九三平方和，可以如下操作：


nums = [1,2,3,4,5,6]

# s = sum(x*x for x in nums)
# print(s)

# Determine if any .py files exist in a directory

import os
dirname = '/home/karson/Recoding_Python/test/'
files = os.listdir(dirname)
if any(name.endswith('.py') for name in files):
    print("There be python.")
else:
    print('Sorry,no python.')

# Output a tuple as csv
s = ("ACME",50,123.45)
print(",".join(str(x) for x in s))

# Data reduction across fields of a data structure

portfolio = [
    {'name':"GOOG",'shares':50},
    {'name':"YHOO",'shares':75},
    {'name':"AOL",'shares':20},
    {'name':"SCOX",'shares':65}
]


min_shares = min(s['shares'] for s in portfolio)
print(min_shares)


# 1.19.3 讨论
# 　这种解决方案展示了当把生成器表达式作为函数的单独参数时在语法上的一些微妙之处（即不必重复使用括号）。比如，下面
# 这两行代码表示的是同一个意思

s = sum((x*x for x in nums)) # Pass generator-expr as argument
s1 = sum(x*x for x in nums) # More elegant syntax

# 比起首先创建一个临时的列表，使用生成器做参数通常是更高效和优雅的方式。例如
# 如果不使用生成器表达式，可能会考虑下面这种实现：


nums1 = [1,2,3,4,5,6]
s2 = sum([x*x for x in nums1])

# 这也能工作，但这引入了一个额外的步骤而且创建了额外的列表。对于这么小的一个列表，这根本就无关紧要。
# 　但是如果nums非常巨大，那就会创建一个庞大的临时数据结构，而且只用一次就要丢弃。
# 基于生成器的解决方案可以以迭代的方式转换数据，因此在内存使用上要高效得多

# 　某些特定的换算函数比如　min(),max()都可接受一个key参数，当可能倾向于使用生成器时会很有帮助。
# 例如在portfolio的例子中，也许会考虑下面的这种替代方案：

# Original: Returns 20

min_shares1 = min(s['shares'] for s in portfolio)

print(min_shares1)

# Alternative:Returs {'name':'AOL','shares':20}

min_shares2 = min(portfolio,key=lambda s:s['shares'])
print(min_shares2)