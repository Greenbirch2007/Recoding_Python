# ７．６　定义匿名或内联函数
# ７．６．１　问题
# 我们需要提供一个短小的回调函数为sort()这样的操作所用，但是又不想通过def语句编写一个单行的函数。相反
# 我们更希望能有一个简便的方式来定义"内联"式函数


# ７．６．２　解决方案
# 像这种仅仅完成表达式求值的简单函数可以通过lambda表达式来代替，如下

add = lambda x,y: x+y
print(add(2,3))
print(add("hello","world"))

# 这里用到的lambda表达式与下面函数定义效果相同


def add(x,y):
    return x + y

# 一般来说，lambda表达式可用在如下的上下文环境中，比如排序或对数据进行整理时


names =['David Beazley','Brian Jones','Raymond Hettinger']
print(sorted(names,key=lambda name:name.split()[-1].lower()))

# 7.6.3

# 尽管lambda表达式允许定义简单的函数，但它的局限性很大。我们只能指定一条单独的表达式，这个表示的结果就是函数
# 返回值。这意味着其他语言特性，比如多行语句，条件分支，迭代和异常处理统统都无法使用
# 如果需要编写很多微型函数来对各表达式进行求值，或在需要用户提供回调函数的时候，这时lambda表达式救恩给你排上用场