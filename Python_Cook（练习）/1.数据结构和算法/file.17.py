# 1.17 从字典中提取子集
# 1.17．1 问题

# 　我们想创建一个字典，其本身是另一个字典的子集

# 1.17.2 解决方案

# 　利用字典推导式(dictionary comprehension)  可轻松解决　　如：

prices ={
    'ACME':45.23,
    'AAPL':612.78,
    'IBM':205.55,
    'HPQ':37.20,
    'FB':10.75
}

# Make a dictionary of all  prices over 200
p1 = {key:value for key,value in prices.items() if value > 200}
print(p1)
# Make a dictionary of tech stocks

tech_names = {'AAPL','IBM','HPQ','MSFT'}
p2 = {key:value for key,value in prices.items() if key in tech_names}
print(p2)

# 1.17.3 讨论

# 大部分可以用字典推导式解决的问题也可以通过创建元组序列然后将它们传给dict()函数来完成　例如：
p1 = dict((key,value) for key,value in prices.items() if value > 200)
print(p1)

# 但是字典推导式的方案更加清晰，而且实际运行起来也要快很多(效率要快２倍)

# 有时候会有多种方法来完成同一件事情。例如，第二个例子还可以重写成：

# Make a dictionary of tech stocks

tech_names = ['AAPL','IBM','HPQ','MSFT']
p2 = {key:prices[key] for key in prices.keys() & tech_names}
print(p2)

# 但是，计时测试表明这种解决方案要比第一种慢１．６倍。如果需要考虑性能因素，那么通常都需要花一点时间
# 来研究它。有关计时和性能分析方面的信息，详见　１４．１３
