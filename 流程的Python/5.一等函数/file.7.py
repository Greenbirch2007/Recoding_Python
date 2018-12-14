# 5.7  从定位参数到仅限关键字参数
# python一大特性即使提供了极为灵活的参数处理机制，而且Python3进一步提供了仅限关键字参数(keyword-only argument).与之密切香瓜的是，
# 调用时使用*和**"展开"可迭代对象，映射到单个参数。

#　示例5.10  tag函数用于生成HTML标签，使用名为cls的关键字参数传入"class"属性，这是一种变通的方法，因为"class"是python的关键字

def tag(name,*content,cls=None,**attrs):
    '''生成一个或多个HTML标签'''
    if cls is not None:
        attrs['class']  = cls

    if attrs:
        attrs_str = ''.join(' %s=%s' %(attr,value)
                            for attr,value
                            in sorted(attrs.items()))

    else:
        attrs_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>'%(name,attrs_str,c,name) for c in content)

    else:
        return '<%s%s/ > ' %(name,attrs_str)


# tag函数的调用方式很多，
# 示例 5.11 tag函数 充多调用方式中的几种

# print(tag('br'))
# print(tag('p','hello'))
# print(tag('p','hello',id=33))
# print(tag('p','hello','world',cls='sidebar'))
# print(tag(content='testing',name='img'))
#
# my_tag = {'name':'img','title':'Sunset_Boulevard','src':'sunset.jpg','cls':'framed'}
# print(tag(my_tag))
# 传入单个定位参数，生成一个指定名称空标签
# 第一个参数后面的任意个参数会被*content捕获，存入一个元组。
# tag函数签名中灭有明确指定名称的关键字参数会被**attrs捕获，存入一个字典
# cls参数只能作为关键字参数传入
# 调用tag函数时，即便第一个定位参数也能作为关键字参数传入
# 在my_tag前面加上**,字典中的所有元素作为单个参数传入，同名键会绑定到对应的具名参数上，余下的则被**attrs捕获

# 仅限关键字参数是python3新增的特性。在示例５．１０中，cls参数只能通过关键字参数指定，它一定不会捕获未命名的定位参数。定义函数时若想指定仅限
# 关键字参数，要把它们放到前面有*的参数的后面。如果不想支持数量不定的定位参数，但是想支持仅限关键字参数，在签名中放一个*，如下

def f(a,*,b):
    return a,b
print(f(2,b=3))
# 注意，仅限关键字参数不应要有默认值，可以像上面b那样，强制必须传入一个实参
# 下面说明函数参数的内省，以一个web框架的示例作为引子，然后再来讨论内省技术