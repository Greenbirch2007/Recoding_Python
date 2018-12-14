# ９．４　　classmethod与staticmethod

# classmethod，定义操作类，而不是操作类示例的方法。classmethod改变了调用方法的定义，因此类方法的第一个参数是类本身，而不是示例
# classmethod最常见的用途是定义备选构造方法，如示例中的frombytes.注意，frombytes的最后一行使用cls参数构建了一个新实例，即cls(*memv)
# 按照约定，类方法的第一个参数名为cls

# staticmethod装饰器也会改变方法的调用方法，但是第一个参数不是特殊的值。其实，静态方法也是就是普通的函数，只是碰巧在类的定义体中而不是在模块层
# 定一。
#　示例９．４　　　比较classmethod和staticmethod的行为



class Demo:
    @classmethod
    def klassmeth(*args):  # 第一个参数始终是Demo类
        return args

    @staticmethod
    def stameth(*args):
        return args


print(Demo.klassmeth())
print(Demo.stameth())
print(Demo.klassmeth('spam'))
print(Demo.stameth('spam'))

# classmehod装饰器非常有用，但是staticmethod不是很常用。如果想定义不需要与累交互的函数，那么在模块中定义即可。
#　有时，函数虽然从不处理类，但是函数的功能与类紧密相关，因此想把它放在进出。即便如此，在同一模块中的类前面或后面定义函数可