#  第20章  属性描述符


#  描述符是对多个属性运用相同存取逻辑的一种方式.例如,Django ORM 和SQL Alchemy等ORM中的字段类型是描述符,把数据库记录中字段里的数据与Python
#  对象的属性对应起来


#  描述符是实现了特定协议的类,这个协议包括__get__,__set__,__delete__方法.property类实现了完整的描述符协议.
#  通常,可以只实现部分协议.其实,我们在真实的代码中见到的大多数描述符只实现了__get__和__set__方法

#  描述符是python的独有特征,不仅在应用层中使用,在语言的基础设施中也有用到.除了特性之外,使用描述符的python功能还有方法及classmethod和staticmethod装饰器
#  理解描述符是精通python的关键.


#  20.1  描述符示例:验证属性

#  特性工厂函数借助函数式编程模式避免重复编写读值方法和设值方法.特性工厂函数是高阶函数,在闭包中存储storage_name等设置,由参数决定创建哪些存取函数,
#  再使用存取函数构建一个特性实例.解决这种问题的面向对象方式就是描述符类

#  20.1.1 LineItem类第3版: 一个简单的描述符


#  实现了__get__,__set__或 __delete__方法的类是描述符.描述符的用法是,创建一个实例,作为另一个类的类属性


#  我们将定义Quantity描述符,LineItem类会用到两个Quantity实例:一个用于管理weight属性,另一个用于管理price属性

#  从现在开始,进行如下定义

#  1. 描述符类

#  实现描述符类
#  2. 托管类

#  把描述符实例声明为类属性的类

# 3. 描述符实例
#  描述符类的各个实例,声明为托管类的类属性,

#  4. 托管实例
#  托管类的实例

#  5. 存储属性

#  托管实例中存储自身托管属性的属性.LineItem实例的weight和price属性是存储属性.这种属性与描述符属性不同,描述符属性都是类属性


#  6. 托管属性

#  托管类中描述符实例处理的公开属性值存储在存储属性中,描述符实例和存储属性为托管属性建立了基础


#  Quantity实例是LineItem类的类属性,

#  示例 20-1  使用Quantity描述符管理LineItem的属性

# class Quantity:
#
#     def __init__(self,storage_name):
#         self.storage_name =storage_name
#
#
#     def __set__(self, instance, value):
#         if value > 0:
#             instance.__dict__[self.storage_name] = value
#
#         else:
#             raise ValueError('value must be > 0')
#
#
# class LineItem:
#
#     weight = Quantity('weight')
#     price = Quantity('price')
#
#     def __init__(self,description,weight,price):
#         self.description = description
#         self.weight = weight
#         self.price = price
#
#     def subtotal(self):
#         return self.weight * self.price


# 1.描述符给予协议实现,无需创建子类
#  2. Quantity实例有个storage_name属性,这是托管实例中存储值的属性的名称

#  3.尝试为托管属性赋值时,会调用__set__方法.这里,self是描述符实例(即LineItem.weight或LineItem.price),instance是托管实例(LineItem实例)
#  value是要设定的值

#  4. 这里,必须直接处理托管实例的__dict__属性;如果使用内置的setattr函数,会再次触发__set__方法导致无限递归

#  5. 第一次描述符实例绑定给weight属性
#  6. 第二个描述符实例绑定给price属性

#  7. 类定义体重余下的代码

#  各个托管属性的名称与存储属性一样,而且读值方法不需要特殊的逻辑,所以Quantity类不需要定义__get__方法
#
# t = LineItem("w",100,0)
# print(t)

# 编写__set__方法时,要记住self和和instance参数的意思:
#  self是描述符实例,instace是托管实例.管理实例属性的描述符应该把值存储在托管实例中.因此Python才为描述符中的那个方法提供了instance参数

#  注意,把各个托管属性的值直接存在描述符实例中.可以想想想__set__方法前两个参数(self和instance)这里,self是描述符实例,它其实是托管类的类属性
#  同一时刻,内存中可能有几千个LineItem实例,不过只会有两个描述符实例:LineItem.weight和LineItem.price.因此,存储在描述符实例中的数据,其实会变成LineItem类
# 的类属性,从而由全部LineItem实例共享

# 上面在托管类的定义体中实例化描述符时要重复输入属性的名称

#　赋值语句右手变的表达式先执行，而此时变量还存在．Quantity()表达式计算的结果是创建描述符，而此时Quantity类中的代码无法猜出要把
#　描述符绑定都给哪个变量(weight或price)

#　解决这个重复输入名称的问题．最好使用类装饰器或元类．但是下面给出一种解决方法

# 20.1.2  LineItem类第４版：　自动获取存储属性的名称

# 为了避免在描述符声明语句中重复输入睡醒名，我们将为每个Quantity实例的storage_name属性生成一个独一无二的付　

# 　为了生成storage_name,我们以"_Quantity#"为前缀，然后在后面拼接一个整数：Quantity.__counter类属性的当前值，每次把一个新的Quantity描述符是依附
# 到类上，都会递增这个值．在前缀中使用井号能避免storage_name与用户使用点号创建的属性冲突，因为nutmeg._Quantity#0是无效的python句法
# 但是，内置的getattr和setattr函数可以使用这种"无效的"标识符获取和设置属性，此外也可以直接处理实例属性__dict__.


# 示例２０－２　　每个Quantity描述符都有独一无二的storage_name


# class Quantity:
#
#     __counter = 0  # 1.
#
#
#     def __init__(self):
#         cls = self.__class__ # 2.
#         prefix = cls.__name__
#         index = cls.__counter
#         self.storage_name = "_{}#{}".format(prefix,index) # 3.
#         cls.__counter += 1 # 4.
#
#
#     def __get__(self, instance, owner):  # 5.
#         return getattr(instance,self.storage_name)
#
#     def __set__(self, instance, value):
#         if value > 0:
#             setattr(instance,self.storage_name,value)  # 7.
#         else:
#             raise ValueError('value must be > 0')
#
# class LineItem:
#     weight = Quantity()
#     price = Quantity()
#
#     def __init__(self,description,weight,price):
#         self.description = description
#         self.weight = weight
#         self.price = price
#
#
#     def subtotal(self):
#         return self.weight * self.price

# 1. __counter是 Quantity类的类属性，统计Quantity实例的数量
#  2. cls是Quantity类的引用
#  3. 每个描述符实例的storage_name属性都是独一无二的,因为其值由描述符类的名称和__counter属性的当前值构成(例如,_Quantity#0)
#  4. 递增__counter属性的值
#  5. 我们要实现__get__方法,因为托管属性的名称与storage_name不同.
#  6. 使用内置的getattr函数从instance中存储属性的值
#  7. 使用内置的setattr函数把值存储在instance中
#  8. 现在,不用把托管属性的名称传给Quantity构造方法.


#  这里可以使用内置的高阶函数getattr和setattr存取值,无需使用instance.__dict__,因为托管属性和存储属性的名称不同,所以把存储属性传给getattr函数
#  不会触发描述符,下面示例,weight和price描述符能按预期使用,而且存储属性也能直接读取----对调试有帮助


# co = LineItem("Brazilian C",20,18)
# print(co.price,co.weight)
# print(88*'~')
#
# print(getattr(co,'_Quantity#0'))

# 注意,__get__方法有3个参数,self,instance和owner.owner参数是托管类(如LineItem)的引用,通过描述符从托管类中获取属性时用得到.如果使用LineItem.weight
# 从类中获取托管属性(以weight为例)，描述符的__get__方法收到的instance参数值是None

# 此外，为例给用户提供内省和其他元编程计数支持，通过类访问托管属性时，最好让__get__方法你会描述符实例．


# 示例20-3  通过托管类调用时,__get__方法返回描述符的引用

class Quantity:
    __counter = 0

    def __init__(self):
        cls = self.__class__
        prefix = cls.__name__
        index = cls.__counter
        self.storage_name = '_{}#{}'.format(prefix,index)
        cls.__counter += 1

    def __get__(self, instance, owner):
        if instance is None:
            return self  #如果不是通过实例调用，返回描述符自身

        else:
            return getattr(instance,self.storage_name) # 否则，发挥托管属性的值


    def __set__(self, instance, value):
        if value > 0:
            setattr(instance,self.storage_name,value)

        else:
            raise ValueError('value must be > 0')




class LineItem:
    weight = Quantity()
    price = Quantity()

    def __init__(self,description,weight,price):
        self.description = description
        self.weight = weight
        self.price = price


    def subtotal(self):
        return self.weight * self.price


print(LineItem.price)

br = LineItem('BAS',10,20)
print(br.price)


# 整洁的LineItem类：Quantity描述符现在位于导入的model_4c模块中，导入这个模块，指定一个更友好的名称

# 使用model.Quantity描述符

#  Django模型的字段就是描述符

# 描述符的优点：
#  １．　描述符类可以使用子类扩展；若想重用工厂函数中的ｄｉａｍ，除了复制粘贴，很难有其他方法
#  ２．　示例中，使用函数数属性和闭包保持状态相比，在类属性和实例属性中保持状态更易于理解
#  在某种程度上，特性工厂函数模式较简单，可是描述符类方式更易于扩展，应用也更多


#  ２０．１．３　　LineItem类第５版：一种新型描述符


#  回想Quantity的功能，它值做了两件事：
#  １．管理托管实例中搞得存储属性，　（管理存储的值）
#  ２．验证用于设置那两个属性的值　　(验证它)

#  创建两个基类

#  AutoStorage   自动管理存储属性的描述符类
#  Validated     扩展AutoStorage类的抽象子类，覆盖__set__方法，调用必须由子类实现的validate方法

# 我们会重写Quantity类，并实现NonBlank,让它继承Validated类，只编写validate方法

#  几个描述符类的层次结构
#　1.AutoStorage基类　　负责自动存储属性；
#　２．　Ｖalidated类做验证，把职责委托给抽象方法validate
#　3.  Quantity和NonBlank是Validated的具体　子类


#　Validated,Quantity和NonBlank三个类之间的关系体现了模板方法设计模式．具体而言，Validated.__set__方法正是Gamma等四人所描述的模板方法的例证
#　一个模板方法用一些抽象的操作定义一个算法,而子类将冲定义这些操作以提供具体的行为.  抽象的操作是验证

#　示例20-6  重构后的描述符类

# 示例２０－７　　使用Quantity和NonBlank描述符的LineItem类

import model_v5 as model  # 导入model_v5模块，指定一个友好的名称


class LineItem:
    description = model.NonBlank()# 使用mode.NonBlank描述符，其他代码没变
    weight = model.Quantity()
    price=  model.Quantity()


    def __init__(self,desciption,weight,price):
        self.description = desciption
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


# 本章锁具的几个LineItem实例演示了描述符的典型用户，管理数据属性．这种描述符叫做覆盖型描述符，因为描述符的__set__方法使用托管实例中的同名
# 属性覆盖(即插手接管)了要设置的苏醒．不过，有非覆盖型的描述符．下节看看这两种描述符的区别

