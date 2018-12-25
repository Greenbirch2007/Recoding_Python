# #　１９．３　特性全解析
#
# #　虽然内置的property经常用做装饰器，但它其实是一个类，在python中，函数和类通常可以互换，因为二者都是可调用的对象，而且没有实例化对象的new运算符
# #　所以调用构造方法与调用工厂函数没有区别／此外，只要能返回新的可调用对象，代替被装饰的函数，二者都可以用作装饰器
#
# #　property 构造方法的完整前面如下：
#
# #　　property(fget=None,fset=None,fdel=None,doc=None)
#
# #　所有参数都是可选　的，如果没有把函数传给某个参数，那么得到的特性对象就不允许执行响应的操作
# #　property 在python2.4之前都不是装饰器，所以若想定义特性，则只能把存取函数传给前两个参数．
#
# #　不使用装饰器定义特性的"经典句法如下"
#
# class LI:
#
#     def __init__(self,description,weihgt,price):
#         self.description =description
#         self.weihgt = weihgt
#         self.price  = price
#
#
#     def subtotal(self):
#         return self.weihgt * self.price
#
#
#     def get_weight(self):
#         return self.__weight
#
#     def set_weight(self,value):
#         if value > 0:
#             self.__weight = value
#         else:
#             raise ValueError('value must be >0')
#     weight = property(get_weight,set_weight)
#
# # 1.普通的读值方法
# # 2.普通的设值方法
# #  ３．构建property对象，然后赋值给公开的类属性
#
# #  某些情况下，这种经典形式比装饰器语法好：烧好讨论的特性工厂函数就是一个例子，但是在方法众多的类定义体中使用装饰器的化，一眼就能看出
# #  哪些是读值方法，哪些是设值方法，而不用按照惯例，在方法名的前面加上get和set
#
# #  类中的特性能影响实例属性的寻找方式，而一开始这种方式可能会让人觉得意外
#
# #  １９．３．１　　特性会覆盖实例属性
#
#
# #  特性都是类属性，但是特性惯例的其实是实例属性的存取
#
# #  如果实和所属的类有同名数据属性，那么实例属性会覆盖(或遮盖)类属性---至少通过那个实例读取属性时是这样
#
#
# #  示例１９－１９　　实例属性覆盖类的数据属性

class Clas: # 1.定义Clas类，这个类有两个类属性：data数据属性和prop特性
    data = ' the class data attr'
    @property
    def prop(self):
        return 'the prop vlaue'

obj = Clas()
print( '2. vars函数返回obj的__dict__属性，表示没有实例属性:        vars(obj) ')
print(' ３．读取obj.data，获取的是Clas.data的值               obj.data')
obj.data = 'bar'# 4.为obj.data赋值，创建一个实例属性
print(' 5.审查实例，查看实例属性                   vars(obj)')
print(obj.data) # 6.现在读取obj.data,获取的是实例属性的值.从obj实例中读取属性时,实例属性data会覆盖类类属性data
print(Clas.data) # 7. Clas.data属性的值完好无损

#
# # 下面尝试覆盖obj实例的prop特性.
#
# # 示例19-20  实例属性不会覆盖类特性
#
# print(88*'~')
print(Clas.prop)
print(obj.prop)
# obj.prop = 'foo~~~'
obj.__dict__['prop']= 'foo'
print(vars(obj))
print(obj.prop)
Clas.prop = 'baz'
print(obj.prop)
#
# # 1.直接从Clas中读取prop特性,获取的是特性对象本身,不会运行特性的读值方法
# # 2.读取obj.prop会执行特性的读值方法
# # 3.尝试设置prop实例属性,结果失败
# # 4.但是可以直接把"prop"存入obj.__dict__
# # 5.可以看到,obj现在有两个实例属性:data和prop
# # 6. 然而,读取obj.prop时仍会运行特性的读值方法,特性没有被实例属性覆盖
# # 7.覆盖Clas.prop特性,销毁特性对象
# # 8. 现在,obj.prop获取的是实例属性.Clas.prop不是特性了,因此不会再覆盖obj.prop
#
# # 再举一个例子,为Class类新添一个特性,覆盖实例属性.
#
#
# # 示例19-21  新添的类特性覆盖现有的实例属性
print(88*'_-_')
print(obj.data ) # obj.data获取的是实例属性data
print(Clas.data)  # Clas.data获取的是类属性data
Clas.data = property(lambda self: 'the "data" prop value ')  # 使用新特性覆盖Clas.data
print(obj.data) # 现在,obj.data被Clas.data特性覆盖了
del Clas.data  # 删除特性
print(obj.data) # 现在恢复原样,obj.data 获取的是实例属性data

#　本节的观点是，obj.attr这样的表达式不会从obj开始寻找attr，而是从obj.__class__开始，而且，仅当类中没有名为attr的特性时，python才会
#  在obj实例中寻找．这条规则不仅适用于特性，还适用与一整类描述符---覆盖型描述符(overriding descriptor)．特性其实是覆盖型描述符

#  现在回到特性．各种python代码单元(模块，函数，类和方法)都可以有文档字符串．下一些说明如何把文档依附到特性上


#  １９．３．２　　特性的文档


#  控制台的help()函数或ide等工具需要显示特性的文档，会从特性的＿doc__属性中提取信息

#  如果使用经典调用句法，为property对象设置文档字符串的方法是传入doc参数
# weight = property(get_weight,set_weight,doc="weight in kilograms")
# 使用装饰器创建property对象时，读值方法(有@property装饰器的方法)的文档字符串作为一个整体，变成特性的文档．

#  示例19-22  特性的文档

class Foo:

    @property
    def bar(self):
        ''' The bar attribute'''
        return self.__dict__['bar']

    @bar.setter
    def bar(self,value):
        self.__dict__['bar'] = value

# 保护LineItem对象的weight和price属性，只允许设为大于零的值；但是，不用手动实现两对几乎一样的读值和设值方法



