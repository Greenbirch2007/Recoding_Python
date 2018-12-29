
#　重构的描述符类



import abc

class AutoStorage:  # 1. AutoStorage提供了之前Quantity描述符的大部分功能
    __counter = 0

    def __init__(self):
        cls = self.__class__
        prefix = cls.__name__
        index  = cls.__counter
        self.storage_name = '_{}#{}'.format(prefix,index)
        cls.__counter += 1



    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return getattr(instance,self.storage_name)


    def __set__(self, instance, value):
        setattr(instance,self.storage_name,value) # 2.验证除外


class Validated(abc.ABC,AutoStorage):  # 3. Validated是抽象类,不过也继承子AutoStorage类

    def __set__(cls, instance, value):
        value = cls.validate(instance,value)  # 4. __set__方法把验证操作委托给validate方法
        super().__set__(instance,value) # 继承父类AutoStorage的__set__方法  # 5.然后把返回的value传给超类的__set__方法,存储值



    @abc.abstractclassmethod  # 变成了抽象方法,如果不专门调用,就不能被实例化
    def validate(cls,instance,value):   # 6. 在这个类中,validate是抽象方法 (起到保护作用)
        '''return validated value or raise ValueError'''


class Quantity(Validated):  # 7.Quantity和NonBlank都继承子Validated类
    '''a number greater than zero'''

    def validate(cls,instance,value):
        if value <= 0:
            raise ValueError('Value must be > 0')
        return value

class NonBlank(Validated):
    """ a string with at least one one-space character """

    def validate(cls,instance,value):
        value = value.strip()
        if len(value) == 0:
            raise  ValueError('value cannot be empty or blank')
        return value  # 8.


# 8. 要求具体的validate方法返回验证后的值,接机可以清理,转换或规范化接收的数据.这里,我们把value首尾的空白去掉,然后将其返回

#　model_v5.py脚本的用户不需要知道全部细节．用户只需知道，它他们可以使用Quantity和NonBlank自动验证实例属性．



def entity(cls): # 1.装饰器的参数是一个类
    for key,attr in cls.__dict.items(): # 2.迭代存储类属性的字典
        if isinstance(attr,Validated): # 3. 如果属性是Validated描述符的实例
            type_name = type(attr).__name__
            attr.storage_name = '_{}#{}'.format(type_name,key)  # 4.  使用描述符类的名称和托管的名称命名storage_name(如_NonBlank#description)

    return cls # 5. 返回修改后的类

