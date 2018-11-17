# 9.21  避免出现重复的属性方法
# ９．２１．１　问题
# 我们正在编写一个类，而我们不得不重复定义一些执行了相同任务的属性方法，比如做类型检查，我们要简化代码

# ９．２１．２　解决方案
# 考虑下面这个简单的类，这里的属性都用property方法进行包装



class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        if not isinstance(value,str):
            raise  TypeError('name must be a  string')
        self._name =value

    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,value):
        if not isinstance(value,int):
            raise  TypeError('age must be an int')
        self._age = value


# 一种解决方法就是创建一个函数，让它为我们定义这个属性并返回给我们


def typed_property(name,expected_type):
    storage_name = '_' + name

    @property
    def prop(self):
        return getattr(self,storage_name)

    @prop.setter
    def prop(self,value):
        if not isinstance(value,expected_type):
            raise TypeError('{} must be a {}'.format(name,expected_type))
        setattr(self,storage_name,value)
    return prop

# example use

class Person1:
    name = typed_property('name',str)
    age = typed_property('age',int)
    def __init__(self,name,age):
        self.name = name
        self.age = age

# 9.21.3  讨论

# 　闭包的使用，可以使用　　functools.partial()

from functools import partial

String = partial(typed_property,expected_type=str)
Integer = partial(typed_property,expected_type=int)

# example

class Person2:
    name = String('name')
    age  = Integer('age')
    def __init__(self,name,age):
        self.name  = name
        self.age = age

