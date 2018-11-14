# 9.3 对装饰器进行解包装

#  9.3.1  问题
#  我们已经把装饰器添加到一个函数上了，但是想‘撤销’它，访问未经过包装的那个原始函数

#  ９．３．２　　解决方案
#  假设装饰器的实现中已经使用了＠wraps,一般俩说我们可以通过访问__wrapped__睡醒来获取对原始函数的访问　如下

from functools import wraps


def somedecorator(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        return result
    return wrapper

@somedecorator
def add(x,y):
    return x+y


orig_add = add.__wrapped__
print(orig_add(3,4))

# 9.3.3 讨论
# 直接访问装饰器背后的那个未包装过的函数对于调试，发射(introspection,"自省")以及其他一些设计函数的操作很有保障。
# 但是本节讨论的技术只有在实现装饰器时利用functools模块中的@wraps对元数据进行了适当的拷贝，或直接设定了__wrapped__属性时才有用

# 如果有多个装饰器已经作用于某个函数上了，那么访问__wrapped__属性的行为目前是未定义的，应该避免这种情况
# 在Python3中，这么做会绕过所有的包装层。如下



from functools import wraps

def decorator1(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print('Decorator ~~1~~~')
        return func(*args,**kwargs)
    return wrapper



def decorator2(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print('Decorator ~~2~~~')
        return func(*args,**kwargs)
    return wrapper


@decorator1
@decorator2
def  add(x,y):
    return x+y

# 当调用装饰过的函数已经通过__wrapped__属性调用原始函数时就会出现这样的情况：


print(add(6,6))
print(88*'#')
print(add.__wrapped__(6,9))

# 然而，这种行为已经被报告了一个bug,可能会在今后释出的版本中修改为暴露出合适的装饰器链(decorator chain)

# 请注意，并不是所有的装饰器都使用了@wraps，因此有些装饰器的行为可能与我们的期望有区别
# 特别是，由内建的装饰器@staticmethod,@classmethod创建的描述符(descriptor)对象并不遵循这个约定(相反，它们会把原始函数保存在__function__属性中)
# 所以，具体问题需要具体分析，每个人遇到的情况会不一样