#　１６．３　　示例：使用协程计算移动平均值

#　示例１６－３　　定义一个计算移动平均值的协会才能

def averagetr():
    total = 0.0
    count = 0
    average = None

    while True:
        term = yield average
        total += term
        count += 1
        average = total/count


# 这个无线循环表明，只要调用方不断把值发给这个协程，它就会一直接收值，然后生成结果．仅当调用方在协程上调用.close()方法，或没有对协程
#　的引用而被垃圾回收程序回收时，这个协程才会终止
#　这里的yield表达式用于暂停执行协程，把结果发给调用方；还用于接收调用方后面发给协程的值，恢复无限循环
#　使用协程的好处是，total和count声明为局部变量即可，无需使用实例属性或闭包在多次调用之间保持上下文


#　示例１６－４　　示例的中doctest(单元测试)

coro_avg = averagetr()
next(coro_avg)
print(coro_avg.send(10))
print(coro_avg.send(16))
# １．创建协程对象，２．调用next函数，预激协程　　３．　计算移动平均值，多次调用.send()方法，产出当前的平均值

#　