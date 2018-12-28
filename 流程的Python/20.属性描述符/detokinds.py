###  辅助函数，仅用于显示   ###


def cls_name(obj_or_cls):
    cls = type(obj_or_cls)
    if cls is type:
        cls = obj_or_cls
    return cls.__name__.split('.')[-1]


def display(obj):
    cls = type(obj)
    if cls is type:
        return '<class {}>'.format(obj.__name__)

    elif cls in [type(None),int]:
        return repr(obj)

    else:
        return '<{} object>'.format(cls_name(obj))


def print_args(name,*args):
    pseudo_args = ",".join(display(x) for x in args)
    print('-> {}.__{}__({})'.format(cls_name(args[0]),name,pseudo_args))



###  对这个示例重要的类　　###

class Overriding:  # 1.有__get__和__set__方法的典型覆盖描述符
    '''　也称数据描述符或强制描述符'''

    def __get__(self, instance, owner):
        print_args('get',self,instance,owner) # 2. 在这个示例中,各个描述符的每个方法都调用了print_args函数


    def __set__(self, instance, value):
        print_args('set',self,instance,value)


class OverridingNoGet:  # 3. 没有__get__方法的覆盖型描述符
    '''　没有　＂　__get__＂方法的覆盖型描述符'''

    def __set__(self, instance, value):
        print_args('set',self,instance,value)

class NonOverriding:  # 4. 没有__set__方法,所以这是非覆盖型描述符
    '''也称非数据描述符或覆盖型描述符'''

    def __get__(self, instance, owner):
        print_args('get',self,instance,owner)

class Managed:  #　５．托管类，使用各个描述符类的一个实例

    over = Overriding()
    over_no_get = OverridingNoGet()
    non_over = NonOverriding()

    def span(self): # 6. span方法放在这里做一个对比，因为方法也是描述符
        print('-> Managed.span({})'.format(display(self)))


# 接下来几节，要分析对Managed类及其实例做属性读写时的行为


#