# 5.6 函数内省

# 除了__doc__,函数对象还有很多属性。使用dir函数可以探知一个函数具有的属性，如下


# print(dir(len))
# 其中大多数属性是Python对象共有的。本节讨论与把函数视作对象相关的几个属性，先从__dict__开始

# 与用户定义的常规类一样，函数使用__dict__属性存储赋予它的用户属性。这相当于一宗基本形式的注解。一般来说，为函数随意赋予属性不是常见的做法，
# 但是Django框架这么做了。对short_description,boolen,allow_tags属性的说明。把short_description属性赋予一个方法，Django管理后台
# 使用这个方法时，在记录列表中会出现指定的描述文本

def upper_Case__name(obj):
    return ("%s %s" % (obj.first_name,obj.last_name)).upper()
upper_Case__name.short_description = 'Customer name '

# 下面重点说明函数专有而用户定义的一般对象没有的属性。计算两个属性集合的差集的差集便能得到函数专有属性列表(如下)

# 示例５．９　　列出常规对象没有而函数有的睡醒

class C:pass

obj = C()
def func(): pass

print(sorted(set(dir(func)) - set(dir(obj))))

# 如下是类的实例没有，而函数有的属性列表，也就是用户定义的函数的属性

# 　　__annotations__'             dict               参数和返回值的注解
# __call__                      method-wrapper               实现()运算符，即可调用ＵＩ对象协议
# __closure__                     tuple                 函数闭包，即自由变量的绑定(通常是None)
# __code__                        code                  编译成字节码的函数元数据和函数定义体
# __defaults__                      tuple             形式参数的默认值
# __get__                      method-wrapper        实现只读描述符协议
# __globals__                    dict                 函数所在模块中的全局变量
# __kwdefaults__                 dict                 仅限关键字形式参数的默认值
# __name__                     str                      函数名称
# __qualname__                    str                   函数的限定名称，如Random.choice


# 后面会讨论__defaults__,__code__,__annotations__属性，IDE和框架使用它们条关于函数签名的信息。但是为了什么了解这些属性，要先探讨
# Python为声明函数参数和传入实参所提供的强大句法