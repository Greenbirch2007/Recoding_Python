#  １９．４　定义一个特性工厂函数


#  我们将定义一个名为quantity的特性工厂函数，在这个应用中要管理的属性表示不能为负数或零的量．
#  quantity特性的两个实例：一个用于管理weight属性，一个用于管理price


#  示例１９－２４　　quantity特性工厂函数
def quantity(storagen_name):

    def qty_getter(instance):
        return instance.__dict__[storagen_name]

    def qty_setter(instance,value):
        if value > 0 :
            instance.__dict__[storagen_name] = value
        else:
            raise ValueError(' value must be > 0')

    return property(qty_getter,qty_setter)

#  2.qty_getter函数的第一个参数可以命名为self,因为qty_getter函数不在类定义体中；instance只带要把属性存储其中的LineItem实例
# 　3. qty_getter引用了storage_name,把它保存在这个函数的闭包里；值直接从instance.__dict__中获取，为的是跳过特性，放置无限递归
#  ４．定义　qty_setter函数，第一个参数也是instace
#  5.值直接存到instace.__dict__中，这也是为了跳过特性
#  ６．构建一个自定义的特性对象，然后将其返回

#  quantity特性工厂函数




class LineItem:
    w = quantity('w')
    p = quantity('p')

    def __init__(self,description,w,p):
        self.description =description
        self.w = w
        self.p  = p


    def subtotal(self):
        return self.w * self.p

# 1.使用工厂函数把第一个自定义的特性weight定义为类属性
# 2. 第二次调用，构建另一个自定义的特性，price
#  3.这里，特性已经激活，确保不能把weight设为负数或零
#  ４．这里也用到了特性，使用特性获取实例中存储的值

#  特性是类属性．构建各个quantity特性对象时，要传入LineItem实例属性的名称，让特性管理．可惜，这一行要输入两次weight
#  因为特性根本不知道要绑定哪个类属性名．记住，赋值语句的右边先计算，因此调用quantity()时，weight类属性还不存在
#  如果想改进quantity特性，避免用胡重复输入属性名，的使用类装饰器或使用元类




nutmeg = LineItem('Moluccan nutmeg',8,13.95)
print(nutmeg.w,nutmeg.p)
print(sorted(vars(nutmeg).items()))

# 1. 通过特性读取weight和price,这会覆盖同名实例属性
# 2. 使用vars函数审查nutmeg实例,查看真正用于存储值的实例属性

# 工厂函数构建特性,weight特性覆盖了weight实例属性,因此对self.w或nutmeg.w的每个引用都由特性函数处理,只有直接存取__dict__属性才能跳过特性的处理逻辑

# 在真实的系统中,分散在多个类中的多个字段可能要做同样的验证,此时最好把quantity工厂函数放在实用工具模块中,以便重复实使用.最终可能要重构哪个简单的
# 工厂函数改成更易扩展的描述符类,然后使用专门的子类执行不同的验证

