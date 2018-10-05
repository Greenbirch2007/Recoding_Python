#1.8 与字典有关的计算问题
# 1.8.1 问题　　我们想在字典上对数据执行各式各样的计算（比如，最大值，最小值，排序等）

# 1.8.2 解决方案　　假设有一个字典在股票名称和对应的价格做　了映射:

prices = {
    'ACME':45.23,
    'AAPL':612.78,
    'IBM':205.55,
    'HPQ':37.20,
    'FB':10.75
}

# 为了能对字典内容做些有用的计算，通常会利用zip()将字典的键和值反转过来。例如，
# 下面的代码会告诉我们如何找出价格最低和最高的股票　

min_price = min(zip(prices.values(),prices.keys()))
print(min_price)
print(88*'~')

max_price = max(zip(prices.values(),prices.keys()))
print(max_price)

print(88*'~')

# 同样，要对数据排序只要使用zip()再配合sorted()就可以了，比如
prices_sorted = sorted(zip(prices.values(),prices.keys()))
print(prices_sorted)

print(88*'~')

# 当进行这些计算时，请注意zip()创建了一个迭代器，它的内容只能被消费一次。例如
# 下面的代码是错误的

# prices_and_names = zip(prices.values(),prices.keys())
# print(min(prices_and_names))
# print(max(prices_and_names))


# 1.8.3 讨论　如果尝试子字典上执行常见的数据操作，将会发现它们只会处理键，而不是值。例如

print(min(prices))
print(max(prices))
print(88*'~')
# 这很可能不是我们所期望的，因为实际上我们是尝试对字典的值做计算。可以利用字典的values()方法来解决这问题
print(min(prices.values()))
print(max(prices.values()))
# 然而，通常这也不是我们所期望的。比如，我们可能想知道相应的键所关联的信息是什么（例如哪只股票的价格最低？）
# 如果提供一个key参数传递给min()和max(),就能的到最大值和最小值所对应的键是什么。例如
print(88*'~')
print(min(prices,key=lambda k:prices[k]))
print(max(prices,key=lambda k:prices[k]))
print(88*'~')

# 但是，要得到最小值的话，还需要额外执行一次查找。例如：
min_value = prices[min(prices,key=lambda k:prices[k])]
print(min_value)

# 利用了zip()的解决方案是通过将字典的键－值对“反转”　值－键对序列来解决这个问题的
# 当在这样的元组上执行比较操作时，值会先进行比较，然后才是键。这完全符合我们的期望，
# 允许我们用一条单独的语句轻松的对字典里的内容做整理和排序
# 应该要注意的是，当涉及(value,key)对的比较时，如果碰巧有多个条目拥有相同的value值，
# 那么此时key将用来作为判定结果的依据。例如，在计算min()和max()时，如果碰巧value的值
# 相同，则将返回拥有最小或最大key值的那个条目　例如
print(88*'~')
prices = {'AAA':45.23,"ZZZ":45.23}
print(min((zip(prices.values(),prices.keys()))))
print(max((zip(prices.values(),prices.keys()))))