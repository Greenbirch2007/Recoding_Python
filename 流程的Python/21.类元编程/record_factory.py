

def record_factory(cls_name,field_names):
    try:
        field_names = field_names.replace(',',',').split()
    except AttributeError: # 不能调用.replace或.split方法

        pass
    field_names = tuple(field_names)



    def __init__(self,*args,**kwargs):
        attrs = dict(zip(self.__slots__,args))
        attrs.update(kwargs)
        for name,value in  attrs.items():
            setattr(self,name,value)


    def __iter__(self):
        for name in self.__slots__:
            yield getattr(self,name)

    def __repr__(self):
        values = ','.join('{}={!r}'.format(*i) for i
                          in zip(self.__slots__,self))

        return '{}({})'.format(self.__class__.__name__,values)

    cls_attrs = dict(__slots__ = field_names,
                     __init__ = __init__,
                     __iter__ = __iter__,
                     __repr__ = __repr__)
    return type(cls_name,(object,),cls_attrs)


# １．这里体现鸭子类型：尝试在逗号或空格处拆分field_names;如果失败，那么假定field_names本就是可迭代的对象，一个元素对应一个属性名
# 2.使用使用属性名构建元组，这将成为新建类的__slots__属性；此外，这么做还设定了拆包和字符串表示形式中各个字段的顺序
# 3. 这个函数将成为新建类的__init__方法．参数有位置参数和关键字参数
#  4.实现__iter__函数,把类的实例变成可迭代的对象;按照__slots__设定的顺序产出字段值
#  5.实现__slots__和self,生成友好的字符串表示形式
#  6. 组建类属性字典
#  7.调用type构造方法,构建新类,然后将其返回

