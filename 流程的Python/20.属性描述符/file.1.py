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

class Quantity:

    def __init__(self,storage_name):
        self.storage_name =storage_name


    def __set__(self, instance, value):
        if value > 0:
            instance.__dict__[self.storage_name] = value

        else:
            raise ValueError('value must be > 0')


class LineItem:

    weight = Quantity('weight')
    price = Quantity('price')

    def __init__(self,description,weight,price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


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