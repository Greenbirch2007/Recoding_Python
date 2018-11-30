# 示例7.16  使用clock装饰器


import time

from clockdeco import clock



@clock
def snooze(seconds):
    time.sleep(seconds)


@clock
def factorial(n):
    return 1 if n <2 else n*factorial(n-1)


if __name__ =='__main__':
    print(40*'*','Calling snooze(.123)')
    snooze(.123)
    print('*'*40,'Calling factorial(6)')
    print('6!=',factorial(6))


# 现在factorial保存的是clocked函数的引用。自此之后，每次调用factorial(n),执行的都是都是clocked(n)
# 这是装饰器的典型行为：把被装饰的函数换成新函数，二者接受相同的参数，而且(通常)返回被装饰的函数被该返回的值，同事还会做一些额外操作（最后加上奶油的面包）
# 装饰器对函数的作用，相当于要烤面包，和面，加工，装饰器是奶油，自由变量，提前把瓶盖打开（首先会调用），被装饰面包自己加工，等到出炉前，抹上奶油，但是最终还
# 是一个面包，但是是加了奶油的面包。（返回值还是做面包的函数，但是有了其他操作）
#  示例7.15中实现的clock装饰器有几个缺点：不支持关键字参数，而且遮盖了被装饰器函数的__name__和__doc__属性。示例7.17使用functools.wraps装饰器
# 把相关的属性从func复制到clocked中。此外，这个新版还能正确处理关键字采纳数