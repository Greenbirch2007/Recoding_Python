#  8.8 在子类中扩展属性
#  8.8.1 问题 我们想在子类中扩展某个属性的功能，而这个属性是在父类中定义的
#  8.8.2 解决方案

#  考虑如下的代码，我们这里定义了一个属性name:

class Person:
    def __init__(self, name):
        self.name = name

    # Getter function
    @property
    def name(self):
        return self._name

    # Setter function
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value

    # Deleter function
    @name.deleter
    def name(self):
        raise AttributeError("Can't delete attribute")


class SubPerson(Person):
    @Person.name.getter
    def name(self):
        print('Getting name')
        return super().name

    @name.setter
    def name(self, value):
        print('Setting name to', value)
        super(SubPerson, SubPerson).name.__set__(self, value)  ##??? 这种用法第一次见, 作用原理/作用流程是什么?
        # 返回一个父类的实例,然后调用其方法
        # 关键是: super(SubPerson, SubPerson) 如何使用的?

    @name.deleter
    def name(self):
        print('Deleting name')
        super(SubPerson, SubPerson).name.__delete__(self)




s = SubPerson('Guido')
s.name
s.name = 'Karson'
s.name = 88

# 重新定义定义所有的属性方法，并利用super()来调用之前的实现。