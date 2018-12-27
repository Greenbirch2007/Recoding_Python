# python多继承中子类调用父类的同名方法


class A:
    def _a(self):
        print("~~~~A~~~~~")
    def _t1(self):
        print("我是A独有的方法")

class B:
    def _a(self):
        print('~~~~B~~~~~~')

    def _t2(self):
        print('我是B独有的方法')



# class C(A,B):
#     def _a(self):
#         print('~~~~~~~~C~~~~~~')
#
#
# c = C()
# c._a()
# c._t1()
# c._t2()
# 同名方法的情况下,继承也是优先于子类(主动继承)的类的同名方法,如果需要使用父类的同名方法,需要特别处理
# 其他 的非同名方法,则按照广度优先原则进行继承!
# 想在C类中的f_a方法里面使用父类A或者父类B的方法该如何操作呢
# 方法有两种：
# 方法1:  把对象调用转换为类调用

# class C(A,B):
#     def _a(self):
#         A._a(self)
#         print('~~~上面是调用A的同名方法~~~~')
#         B._a(self)
#         print('~~~上面是调用B的同名方法~~~~')
#         print('~~~~~C~~~~~')
#
#
# c = C()
# c._a()

# 这里调用父类的_a方法时括号里面要写self,表明这是一个类调用,但是这种方法有一个缺点,比如说如果修改了父类的名称,哪个在子类中会涉及多处修改,并且python是允许多继承的
# 语言,上述方法在多继承时就要重复写多次,显得累赘,为了解决这些问题,Python引进了super()机制,

#　方法２：使用super()机制，引入super()方法

# class C(A,B):
#     def _a(self):
#         super()._a()  # 不用再写self
#         print('~~~~~上面是写了C继承的父类同名方法～～～～')
#         print('~~~~~C~~~~~')
# c = C()
# c._a()

#  假如想调用B类中的_a方法要如何处理？还是使用super()方法

class C(A,B):
    def _a(self):
        print('~~~~C~~~~`')
        super(C,self)._a() # # 会调用C最左边的父类方法
        super(C,self)._t1() # # 会调用C最左边的父类方法 ，对于父类独有的方法也可以使用
        super(A,self).a()  # 会调用Ａ类后面的那个类的_a方法
        # 如果要继承的不止两个类，如果要调用某个类的方法，只要知道前一个类的类名就可以调用！


c = C()
c._a()

# https://blog.csdn.net/gscsd_t/article/details/79092704#commentBox