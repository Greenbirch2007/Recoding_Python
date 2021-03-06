# 9.17 在类中强制规定编码约定
# ９．１７．１　问题
# 我们的程序由一个庞大的类继承体系组成，我们想强制规定一些编码约定(或做一些诊断工作)，使得维护这个程序的工作轻松一些

# ９．１７．２　　解决方案
# 如果想对类的定义进行监控，通常可以用元类来解决。一个基本的元类通常可以通过从type中继承，然后重定义它的__new__()或__init__()方法即可


class MyMeta(type):
    def __new__(cls,clsname,bases,clsdict):
        # clsname is name of class being defined
        # bases is tuple of base classes
        # clsdict is class dictionary
        return super().__new__(cls,clsname,bases,clsdict)

# 另一种方式是定义__init__()

class Mymeta(type):
    def __init__(self,clsname,bases,clsdict):
        super().__init__(clsname,bases,clsdict)


# 要使用元类，一般来说会将其作用到一个顶层基类上，然后让其他子类继承值。如下


class Root(metaclass=MyMeta):
    pass
class A(Root):
    pass

# 元类的一个核心功能就是允许在定义类的时候对类本身的内容进行检查。在重新定义的__init__()方法中，我们可以自由地检查类字典，基类以及其他更多信息。此外
# 一旦为某个类指定了元类，该类的所有子类都会自动继承这个特性。因此，聪明的框架实现者可以在庞大的类继承体系中为其中一个顶层基类制定一个元类，
# 然后就可以获取到位于该基类之下的所有子类的定义了、
# 下面示例，定义的元类可检查子类中是否有重新定义的方法，确保它们的调用签名和父类中原始的方法相同


# ９．１７．３　　讨论
# 在一个大型的面向对象程序中，有时候通过元类来控制类的定义会十分有用。元类可以监视类的定义，可用来警告程序员那些可能会被忽视的潜在问题（比如使用了不兼容的方法签名）

# 至于在元类中是重新定义__new__()还是__init__()，这取决于我们打算如何使用得到的结果类。__new__()会在类创建之前先得到调用，当元类想以某种方式
# 修改类的定义时(通过修改类字典中的内容)一般会用这种方法。而__init__()方法会在类已经创建完成之后才得到调用，如果想编写代码同完全成形(fully formed)
# 的类对象打交道，那么重新定义__init__()会很有用。在最后那个示例中我们必须重新定义__init__().因为这里用到了super()函数来查找父类中的定义，
# 而这种只有当类实例已经被创建出来且方法解析顺序(MRO)已经设定之后才行得通

# 最后那个示例也展示了对Python函数签名对象的调用。从本质上说，元类首先获取类中的每一个可调用型的定义(函数，方法等)，然后查找它们是否在基类中
# 也有一个定义，如果有的话就通过inspect.signature()来比较它们的调用签名是否一致。

# super(self,self)这行代码并不存在输入错误。当使用元类时，很重要的一点是要意识到self实际上是一个类对象。因此，这行代码实际上是用来寻找
# 位于类层次结构中更高层次上的定义，它们组成了self的父类


