# ８．５　将名称分装到类中

# ８．５．１　问题
# 　我们想将"私有"数据封装到类的实例上，但是又需要考虑到Ｐython缺乏对属性的访问控制问题

# ８．５．２　解决方案
# 与其依赖语言特性来封装数据，Python程序员更期望通过特定的命名规则来表达出对数据和方法的用途。第一个规则是任何以单下划线(_)开头的
# 名字应该总被认为属于内部实现，如下

class A:
    def __init__(self):
        self._internal = 0  # an internal attribute
        self.public = 1  # a public attribute

    def public_method(self):
        ''' a public mehtod'''

    def _internal_method(self):
        pass


#  Python本身并不会阻止其他人访问内部名称。以下划线打头的标识也可用于模块名称和模块级的函数中。比如，如果见到有模块名以下划线打头（例如，_socket）,
# 那么它就属于内部实现。同样地，模块级的函数比如sys.getframe()使用其他也要各位小心
# 我们应该在类定义中也见到过以双下划线(__)打头的名称，如下

class B:
    def __init__(self):
        self.__private = 0

    def __private_method(self):
        pass

    def public_method(self):
        # self.__private_method()
        pass

# 以双下划线打头的名称会导致出现名称重叠(name_mangling)的行为。具体来说就是上面这个类中的私有属性会被分别命名为
#  _B_private 和　_B_private_method.类似这样的名称重整其目的何在？答案就是为了继承————这样的属性不能通过继承而覆盖，如下

class C(B):
    def __init__(self):
        super().__init__()
        self.__private = 1   # Does not override B.__private
        # Does not override B.__private_method()

    def __private_method(self):
        pass

# 这里，私有名称__private和__private_method会被重命名为_C__private  和_C__private_method,这和基类Ｂ中的重整名称不同


# 8.5.3  讨论

# "私有"属性存在两种不同的命名规则(单下划线和双下划线)，这一试试引出了问题：对于大多数代码而言，我们应该让非公有名称以单下划线开头。但是
# 如果我们知道代码中会设计子类化处理，而且有些内部属性应该对子类进行隐藏，那么此时就应该使用双下划线开头

# 此外还应该指出的是，有时候可能想顶一个变量，但是名称可能会和保留字产生冲突，基于此，应该在名称最后加上一个单下划线以示区别如
lambda_ = 2.0

# 合理不采用下划线开头的原因是避免在使用意图上发生混淆。在名称尾部加一个单下划线就能解决这个问题



