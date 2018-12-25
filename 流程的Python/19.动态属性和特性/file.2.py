#  19.2 使用特性验证属性

# 目前,我只介绍了如何使用@property装饰器实现只读特性.本节要创建一个可读写的特性



# 19.2.1  LineItem类第一版:表示订单中商品的类

#  假设有个销售散装有机食物的电商应用,客户可以按重量订购坚果,干果或杂粮.在这个系统中,每个订单中都有一系列商品


class LineItem:

    def __init__(self,description,weight,price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


# 示例19-16  重量为负值时,金额小计为负值


raisins = LineItem('Golden raisins',10,6.95)
print(raisins.subtotal())
raisins.weight = -6
print(raisins.subtotal())

# 这个问题怎么解决? 我们可以修改LineItem类的接口,使用读值方法二和 设值方法管理weight属性,这是java采用的方式
# 但是如果能直接设定商品的weight属性就好.此外,系统可能在生产环境中,而其他部分已经直接访问item.weight了.此时符合python风格的
# 做法,是把数据属性换成特性


#　19.2.2　　LineItem类第２版：能验证值的特性

#　实现特性之后，我们可以使用读值方法和设置方法，但是LineItem类的接口保持不变(即，设置LineItem对象的weight属性依然协程raisins.weight=12)

# 示例１９－１７　　定义了weight特性的LineItem类


#　１．　这里已经使用特性的设值方法了，确保所创建实例的weight属性不能为负值
#　２．　@property装饰器读值方法
#　３．　实现特性的方法，其名称都与公开属性的名称一样－－－weight
#　4. 真正的值存储在私有属性_weight中
#　５．被装饰的读值方法有个.setter属性，这个属性也是装饰器；这个装饰器把读值方法和设值方法绑在一起
#　６．如果值大于零，设置私有属性_weight
#　7. 否则,抛出ValueError异常

#　注意，现在不能创建重量为无效值的LineItem对象

#　也可以把价格的属性设置为特性


#　去除重复的方法是抽象．抽象特性的定义有两种方式：１．使用特性工厂函数　２．或使用描述符类实现的．不过，这里我要继续探讨特性，实现一个特性工厂函数
#　但是，在实现特性工厂函数之前，我们要深入理解特性


