#  19.5  处理属性删除操作


# 对象的属性可以使用del语句删除:     del my_object.an_attribute


# 使用Python编程时不常删除熟悉感,通过特性删除属性更少见.但是,python支持这么做,我们可以虚构一个示例,演示这样处理


#  定义特性时,可以使用@my_property.deleter装饰器包装一个方法,负责删除特性管理的属性.下面说明如何定义特性删除值方法


class BlackKnigt:

    def __init__(self):
        self.members = ['an arm','another arm',
                        'a leg','another leg']
        self.phrases = ['Tis but a scratch.',
                        "It's just a flesh wound.",
                        "I'm invicible!",
                        "All right,we'll call it a draw."]



    @property
    def member(self):
        print('next member is:')
        return self.members[0]

    @member.deleter
    def member(self):
        text = "BLACK KNIGHT (loses {}) \n-----{}"
        print(text.format(self.members.pop(0),self.phrases.pop(0)))

# 对上面类进行单元测试

k = BlackKnigt()
print(k.member)
print(88*'~')

del k.member
print(88*'~')
del k.member
print(88*'~')
del k.member
print(88*'~')
del k.member


# 在不适用装饰器的经典调用句法中,fdel参数用于设置删值函数.例如,在Blacknight类的定义体中可以喜爱给你下面这样创建member特性

member = property(member_getter,fdel=member_deleter)

# 如果不使用特性,还可以实现底层特殊的__delattr__方法处理删除属性的操作,可以虚拟一个类,定义__delattr__方法

#  特性是个强大的功能更,不过有时更适合使用简单的等替代方案