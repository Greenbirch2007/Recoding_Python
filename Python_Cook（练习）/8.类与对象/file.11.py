# 8.11 简化数据结构的初始化过程
# 8.1.1问题
# 我们编写了许多类，把它们当做数据结构来用。但是我们厌倦了编写高度且样式相同的__init__()函数

# 8.1.2  解决方案
# 通常我们可以将初始化数据结构的步骤归纳到一个单独的__init__()函数中，并将其定义为一个公共的基类中。

class Structure:
    # class vaiable that specifies expected fields
    _fields = []
    def __init__(self,*args):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))


        # set that arguments

        for name,value in zip(self._fields,args):
            setattr(self,name,value)

    # example class definitions
    # if __name__ == '__main__':
        class Stock(Structure):
            _fields = ['name','shares','price']

        class Point(Structure):
            _fields = ['x','y']

        class Circle(Structure):
            _fields = ['radius']
            def area(self):
                return math.pi * self.radius **2

        s = Stock('AAPL', 60, 91.1)
        p = Point(2,3)
        c = Circle(4.5)



# 如果使用这些类，就会发现它非常易于构建
# 我们应该提供对关键字参数的支持，这种这里有集中设计上的选择。一种选择是对关键字参数做映射，这样它们就只对应于
# 定义在_fields中的属性名
# 另一种可能的选择是利用关键字参数来给类添加额外的属性，这些额外的属性是没有定义在fields中的

# 8.11.3 讨论
# 如果要编写的程序中有大量小型的数据结构，那么定义一个通用型的__init_()方法会特别有用。
# 精妙之处在于使用了setattr()函数来设定属性值。与之相反的是，有人可能会倾向于直接访问实例字典
# 尽管这么做可以，但是假设子类的实现通常是不安全的。如果某个子类决定使用__slots__或用property(也可以是描述符)包装了
# 某个特定的属性，直接访问实例字典就会产生崩溃。我们给出的解决方案已经尽可能地做到通用，不会对子类的实现做任何假设
# 这种技术的一个潜在缺点就是会影响到IDE(集成开发环境)的文档那和帮助功能。


