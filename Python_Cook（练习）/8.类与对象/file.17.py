# ８．１７　　不通过调用init来创建实例
# 　８．１７．１　　问题
# 我们需要创建一个实例，但是出于某些原因向绕过__init_(),用别的方法来创建

# ８．１７．２　解决方案
# 可以直接调用类的__new__()方法来创建一个未初始化的　实例。采用如下方法可以在不调用__init__()的情况下创建一个Date实例
#
# class Date:
#     def __init__(self,year,month,day):
#         self.year = year
#         self.month = month
#         self.day = day
#
#
# d = Date.__new__(Date)
# print(d)
# 可以看到，得到的实例是未经过初始化的。因此，给实例变量设定合适的初始值现在就成了我们的责任。如下


# data = {'year':2018,'month':11,'day':12}
# for key,value in data.items():
#     setattr(d,key,value)
#
# print(d.day)


# 8.17.3  讨论
# 当需要以非标准的方式来创建实例时常常会遇到需要绕过__init__()的情况。比如反序列化(deserializing)数据，或实现一个类方法将其作为备选的构造函数，
# 都属于这种情况。例如给前面的Date类中，有人可能会定义一个可选的构造函数today()

from time import localtime

class Date:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        d = cls.__new__(cls)
        t = localtime()
        d.year = t.tm_year
        d.month =t.tm_mon
        d.day = t.tm_mday
        return d
# 类似地，假设正在反序列化json数据，要产生一个如下的字典：

# 如果想将这个字典转化为一个Date实例，只要使用解决方案中给出的技术即可

# 当需要以非标准的方式创建实例时，通常最好不要对它们的实现做过多假设。因此，一般来说不要编写直接操纵底层实例字典__dict__的代码
# 除非能够保证它已被定义。否则，如果类中使用了__slots__,property属性，描述符或其他高级技术，那么代码就会崩溃。
# 通过使用setattr()来为属性设定值，代码就会尽可能的通用
