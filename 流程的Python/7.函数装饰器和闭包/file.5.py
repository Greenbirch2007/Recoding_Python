# 7.5 闭包
# 在博客圈，人们有时会把闭包和匿名函数弄混。因为，在函数内部定义函数不常见，知道开始使用匿名函数才会这么做。而且，只有设计嵌套函数时才有闭包问题

# 其实，闭包指延伸了作用域的函数，其中包含函数定义体中引用，但是不在定义体中定义的非全局变量。函数是不是匿名额没有关系，挂件是它能访问定义体职位定义IDE非全局变了
# 假如有一个avg的函数，它的作用是计算不断增加的系列值的均值；例如，整个历史中某个商品的平均收盘价。每天都会增加新价格，因为平均值要考虑值目前为止所有的价格


# avg从哪里来，它又在哪里保存历史值？

# 示例7.8  average_oo.py  计算移动平均值的累


class Averager():
    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total/len(self.series)


# Averager实例是可调用对象
avg = Averager()
print(avg(8))
print(avg(88))
print(avg(888))
print(avg(8888))

# 下面示例7.9是函数式实现，使用高阶函数make_averager

# 示例7.9   average.py  :计算移动平均值的高阶函数

def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)
    return averager

# 调用make_averager时，返回一个averager函数对象。每次调用averager时，它会把参数添加到系列值中，然后计算当前平均值，如下

# 示例7.10  测试示例7.9


avg = make_averager()
print(88*'~')
print(avg(8))
print(avg(88))
print(avg(888))
print(avg(8888))


# 注意，这两个示例的相同之处：调用Averager()或make_averager()得到一个可调用对象avg,它会更新历史值，然后计算当前均值。在示例7.8中
# avg是Averager的实例；在示例7.9中是内部函数averager.不管如何，我们都只需调用avg(n),把n放入系列值中，然后重新计算均值

# Averager类的实例avg在哪里存储历史值很明显：self.series实例属性。但是第二个示例中的avg函数在哪里寻找series呢？
# 注意，series是make_averager函数的局部变量，因为那个函数的定义体中初始化了series:series = [].于是，调用avg(10)时，make_averager函数已经返回了
# 而它的本地作用域也不见了
# 在averager函数中，series是自由变量(free variable).这是一个技术用语，指未在本地作用域中绑定的变量

# 图7.1 averager的闭包延伸到那个函数的作用域之外，包含自由变量series的绑定

# 审查返回的averager对象，我们发现python在__code__属性(表示编译后的函数定义体)中保存局部变量和自由变量的名称
# series的绑定在返回的avg函数的__closure__属性中。avg.__closure__中的哥哥元素对应于avg.__code__.co_freeavars中的一个名称。这些元素是cell对象
# 有一个cell_contents属性，保存这真正的值，如下
# 示例7.11 审查make_averager(见示例7.9) 创建的函数
# 示例7.12 继续测试
print(88*'~')

print(avg.__code__.co_varnames)
print(avg.__code__.co_freevars)
print(avg.__closure__)
print(avg.__closure__[0].cell_contents)

# 综上，闭包是一种函数，它会保留定义函数时存在的自由变量的绑定，这样调用函数时，虽然定义作用域不可用了，然是仍能使用那些绑定
# 注意，只有嵌套在其他函数中的函数才可能需要吃了不在全局组用语中的外部变量