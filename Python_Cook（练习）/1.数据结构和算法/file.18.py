# 　１．１８　　将名称映射到序列的元素中
# 　１．１８．１　问题

# 我们的代码是通过位置(即索引，或下标)　来访问列表或元组的，但有时候这会使得代码难以阅读。
# 我们希望可以通过名称来访问元素，以此减少结构中对位置的依赖性

# 　１．１８．２　解决方案
# 　相比普通的元组，collections.namedtuple()(命名元组)　只增加了极少的开销就提供了这些便利。实际上collections.namedtuple()
#  是一个工厂方法，它返回的是Python中标准元组类型的子类。我们提供给它一个类型名称以及相应的字典，它就返回
# 　一个可实例化的类，为你已经定义好的字典转入值等　如

from collections import namedtuple
Subscriber = namedtuple("Subscriber",['addr','joined'])
sub = Subscriber('jonesy@example.com','2012-10-19')
print(sub)
print(sub.addr)
print(sub.joined)

# 尽管namedtuple的实例看起来像一个普通的类实例，但它的实例与普通的元组是可互换的，而且支持所有支持所有
# 普通元组所支持的操作，例如索引(indexing) 和 分解(unpacking) 比如

print(len(sub))

addr,joined = sub
print(addr)
print(joined)

# 命名元组的主要作用在于将代码同它所控制的元素位置间解耦。所以，如果从数据库调用中得到一个大型的元组列表。而且
# 　通过元素的位置来访问数据，那么假如在表单中新增加一列数据，那么代码就会崩溃。但如果首先将返回的元组转型为命名元组
# 　就不会出现问题
# 为了说明这个问题，下面有一些使用普通元组的代码：

# def compute_cost(records):
#     total = 0.0
#     for rec in records:
#         total += rec[1] + rec[2]
#     return total

# 通过位置来引用元素常常使得代码的表达力不够强，而且也很依赖于记录的具体结构。下面是使用命名元组的版本

from collections import namedtuple

stock = namedtuple('stock',['name','shares','price'])

def compute_cost(records):
    total = 0.0
    for rec in records:
        s = stock(*rec)
        total  += s.shares * s.shares
    return total

# 当然，如果实例中的records序列已经包含了这样的实例，那么可以避免显式地将记录转换为stock命名元组

# 作者的意思是如果records　中的元素是某个类的实例，且已经有了shares和price这样的属性，那就可以直接
# 通过属性名来访问，不需要通过位置来引用，也就没有必要在转换成命名元组了

# １．１８．３　讨论

# namedtuple的一种可能用法是作为字典的替代，后者需要更多的空间来存储。因此，如果要构建涉及字典的大型数据结构，使用
# namedtuple 会更加高效。但请注意的是，与字典不同的是，namedtuple是不可变的(immutable).例如：

s = stock("ACME",100,123.45)
print(s)
# s.shares = 75
# 如果需要修改任何属性，可以通过使用namedtuple实例的_replace()方法来实现。该方法会创建一个
# 全新的命名元组，并对相应的值做替换。如：

s = s._replace(shares=666)
print(s)


# _replace()方法有一个微妙的用途，那就是它可以作为一种简便的方法填充具有可选或缺失字段的命名元组。
# 要做到这点，首先创建一个包含默认值的“原型”元组，然后使用_replace()方法创建一个新的实例，把相应的值替换掉，如下：

print(88*'$')
from collections import namedtuple


stock = namedtuple('stock',['name','shares','price','date','time'])

# Create a prototype instance

stock_prototype = stock(' ',0,0.0,None,None)

# Function to convert a dictionary to a stock

def dict_to_stock(s):
    return stock_prototype._replace(**s)



# 演示代码如下：

a = {'name':'ACME',"shares":100,"price":123.45}
print(dict_to_stock(a))
b = {'name':"ACME","shares":666,"price":6868,'date':'12/7/2018'}
print(dict_to_stock(b))

# 最后，也是很重要的，应该要注意如果我们的目标是定义一个高效的数据结构，而且将来会修改各种实例属性，
# 那么使用namedtuple并不是最佳选择。想法，可以考虑定义一个使用__slots__属性的类。

