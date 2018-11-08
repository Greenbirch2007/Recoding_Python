# 7.9 用函数替代只有单个方法的类
#  7.9.1 问题
#　我们有一个只定义了一个方法的类(除__init__()方法外)。但是，为了简化代码，我们更希望能够只用一个简单的函数来代替

#　７．９．２　解决方案

#　在许多情况下，只有单个方法的类可以通过闭包(closure)将其转换成函数。考虑下面这个例子，这个类允许用户通过某种模板方案来获取URL


from urllib.request import urlopen


class UrlTemplate:
    def __init__(self,template):
        self.template = template

    def open(self,**kwargs):
        return urlopen(self.template.format_map(kwargs))

# example use Download stock data from yahoo

yahoo = UrlTemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')

for line in yahoo.open(names="IBM,AAPL,FB",fields="sllclv"):
    print(line.decode('utf-8'))


# 这个类可以用一个简单函数取代


def rultemplate(template):
    def opener(**kwargs):
        return urlopen(template.format_map(kwargs))
    return opener



#　7.9.3 讨论

#　在许多情况下，我们会使用只有单个方法的类的唯一原因是保存额外的状态给类方法使用
#　使用嵌套函数或闭包更好，闭包就是一个函数，但是它还能保存额外的变量环境，使得这些变量可以在函数中使用。闭包的核心特性就是它可以记住
#　定义闭包时的环境。因此，在这个解决方案中，opener()函数可以记住参数template的值，然后在随后的调用中使用该值。
#　无论何时，当在编写代码中遇到需要附加额外的状态给函数时，请使用闭包