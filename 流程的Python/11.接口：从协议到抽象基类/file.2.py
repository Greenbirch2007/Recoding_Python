# 12.2 多重继承和方法解析顺序
# 新式类，广度

# 示例１２．４　　Ａ,B,C,D４个类


class A:
    def ping(self):
        print('ping:',self)


class B(A):
    def pong(self):
        print('pong:',self)


class C(A):
    def pong(self):
        print('PONG:',self)


# class D(B,A):
#     def ping(self):
#         super().ping()
#         print('post-ping',self)
#
#     def pingpong(self):
#         self.ping()
#         super().ping()
#         self.pong()
#         super().ping()
#         C.pong(self)

#　注意，B和C都实现了pong方法，二者之间唯一的区别是,C.pong方法输出的是大写的PONG
# 在D的实例上调用d.pong()方法的话，运行的是哪个pong方法呢？在C++中，程序员必须使用类名限定方法调用来避免这种奇艺，python也能这么做

# 示例12.5  在D实例上调用pong方法的两种方式


# d = D()

# d.pong()
# C.pong(d)
# 直接调用d.pong()运行的是B类中的版本
#　超类中的方法都可以直接调用，此时要把实例作为显式参数传入

# print(D.__mro__)

# python解析顺序按照方法解析顺序(mro)。类中都有一个名为__mro__的属性，它的值是一个元组，按照方法解析顺序列出各个超累，从当前类一直向上，直到object类
# 如果要把方法调用委托给超类，最好使用的是内置的super()函数，在python3猴子那个，然而有时需要绕开方法解析顺序，直接调用
# 某个超类的方法————

class D(C,B):
    def ping(self):
        A.ping(self)# super().ping()
        print('post-ping',self)

    def pingpong(self):
        self.ping()
        super().ping()
        self.pong()
        super().ping()
        C.pong(self)

print(D.__mro__)
d = D()
d.ping()
d.pong()
print(88*'~')
d.pingpong()
# 注意，直接在类上调用实例方法时，必须显式传入self参数，因为这样访问的是未绑定方法(unbound method)
# 方法解析顺序不仅考虑继承图,还考虑子类声明章列出超类的顺序.如果在上面D类 中声明为D(C,B),那么D类的__mro__属性就会先搜索C类,再搜索B类
