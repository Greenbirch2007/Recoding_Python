#  用def 语句定义的函数是所有程序的基石。本章的内容是向读者展示一些更加高级和独特的函数定义记忆使用模式。主题
# 包括默认参数，可接受任意数量参数的函数，关键子参数、参数注解以及闭包。此外，有关利用回调函数实现巧妙的控制流以及数据传递
# 的问题也有涉及


# ７．１　　编写可接受任意数量参数的函数

# ７．１．１　问题

# 我们向编写一个可接受任意数量参数的函数

# ７．１．２　解决方案
# 要编写一个可接受任意数量的位置参数的函数，可以使用以*开头的参数。示例如下：

def avg(first,*rest):
    return (first + sum(rest)) / (1+len(rest))

# sample use

print(avg(1,2))
print(avg(1,2,3,4))

# 在这个示例中，rest是一个元组，它包含了其他所有传递过来的位置参数。代码在之后的计算中会将其视为一个序列来处理

# 如果要接受任意数量的关键字参数，可以使用以**开头的参数。示例如下：

import html

def make_element(name,value,**attrs):
    keyvals = ['%s=%s'% item for item in attrs.items()]
    attr_str = "".join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(name=name,attrs=attr_str,value=html.escape(value))
    return element

# example
# creates '<item size='large' quantity="6">Albatross</item>'
t = make_element('item','Albatross',size ='large',quantity=6)
print(t)
# creates '<p>&lt;spam&gt'</p>'

t1 = make_element('p','<spam>')
print(t1)

# 在这里attrs是一个字典，它包含了所有传递过来的关键字参数(如果有的话)。如果想要函数能同时接受任意数量的位置参数
# 和关键字参数，只要联合使用*和**即可。示例如下：

def anyargs(*args,**kwargs):
    print(args)  # a tuple
    print(kwargs) # a dict

# 在这个函数中，所有的位置参数都会放置在元组args中，而所有的关键字参数都会放置在字典kwargs中

# ７．１．３　　讨论

# 　在函数定义中，以*开头的参数只能作为最后一个位置参数出现，而以**打头的参数只能作为最后一个参数出现。
# 在函数定义中存在一个很微妙的特性，那就是在*打头的参数后仍然可以有其他的参数新出现

def a(x,*args,y):
    pass

def b(x,*args,y,**kwargs):
    pass
# 这样的参数称之为keyword-only参数(出现在*args之后的参数只能作为关键字参数使用.