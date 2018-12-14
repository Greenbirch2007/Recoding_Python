# 7.6 nonlocal声明

# 改进前面的示例，更好的实现方式是，只存储目前的总值和元素个数，然后使用这两个数计算均值

# 示例7.13  计算移动平均值的高阶函数，不保存所有历史值，但有缺陷

# def make_averager():
#     count = 0
#     total = 0
#     def averager(new_value):
#         count += 1
#         total += new_value
#         return total/count
#
#     return averager

# 上面代码会出错，因为我们没有给series复制，我们只是调用series.append,并把它传给sum和len。也就是利用了列表的可变的性质

# 但是对数字，字符串，元组等不可变类型来说，只能读取，不能更新。其实会隐式创建局部变量count.这样，count就不是自由变量了，因为不会保存在闭包中

# 为了解决这个问题，Python3引入了nonlocal声明。它的作用是把变量标记为自由变量，即使在函数中为变量赋新值，也会变成自由变量。如果为nonlocal
# 声明的变量赋予新值，闭包中保存的绑定会更新。

# 示例7.14  计算移动平均值，不保存所有历史，使用(nonlocal修正)

def make_averager():
    count = 0
    total = 0
    def averager(new_value):
        nonlocal  count,total
        count += 1
        total += new_value
        return total/count

    return averager

# 对付没有nonlocal的Python2
# 处理方式是把内部函数需要修改的变量(如count和total)存储为可变对象(如字典或简单的实例)的元素或属性，并且吧那个对象绑定给一个自由变量
# 至此，我们了解了闭包。下面可以使用嵌套函数来正式实现装饰器