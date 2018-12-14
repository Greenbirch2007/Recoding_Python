# ５．８　　获取关于参数的信息
# HTTP微框架Bobo中有个使用函数内省的好例子。示例５．１２　是对Bobo教程中“hello world”应用的改编，说明了内省怎么使用

# 5.12  Bobo知道hello需要person参数，并且从HTTP请求中获取它

import bobo


@bobo.query('/')
def hello(person):
    return 'Hello %s' % person
# bobo.query装饰器把一个普通的函数(如hello)与框架的请求处理机制集成起来了。装饰器后续会讨论，这不是示例的关键。这里的关键是
# Bobo会内省hello函数，发现它需要一个名为person的参数，然后从请求中获取那个名称对应的参数，将其传给hello函数。

# Bobo知道调用hello函数必须传入person参数，但是在请求中找不到同名参数
# 示例５．１３　如果请求中缺少函数的参数，Bobo返回403forbidden响应，curl -i 的作用是把首部转储到标准输出

# $ curl -i http://locahost:8080/   响应４０３
# 示例5.14 传入所需的person参数才能得到ok响应
# $ curl -i http://locahost:8080/?person=jim   响应200


# Bobo是怎么知道函数需要哪个参数的呢？它又是怎么知道参数有没有默认值呢？
# 函数对象有一个__defaults__属性，它的值是一个元组，里面保存这定位参数和关键字参数的默认值。仅限关键字参数的默认值在__kwdefaults__属性中。
#　然而额，参数的名称在__code__属性中，它的值是一个code对象引用，自身也有很多属性

# 为了说明这些属性的用途，下面在clip.py模块中定义clip函数，如示例5.15所示，然后再审查它


#  示例5.15  在指定长度附近截断字符串的函数

def clip(text,max_len= 80):
    '''在max_len前面或后面的第一个空格处截断文本
    '''
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ',0,max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rind(' ',max_len)
            if space_after >= 0 :
                end = space_after
        if end is None : # 没有找到空格
            end = len(text)

    return text[:end].rstrip()


# 定义clip函数，查看__defaults__,__code__.co_varnames和__code__.co_argcount的值


#　示例５．１６　　提取关于函数参数的信息  使用命令行模式

# from .clip import clip
# print(clip.__defaults__)

# 可以看出，这样组织信息的方式并不是最便利的。参数名称在__code__.co_varnames中，不过里面还有函数定义体中创建的局部变量。
# 因此，参数名称是前N个字符串，N的值由__code__.co_argcount确定。这里不包括前缀为*或**的变长参数，参数的默认值只能通过
# 它们在__defaults__元组中的位置确定，因此要从后向前扫描才能把参数和默认值对应起来。在这个示例中clip函数有两个参数，text和max_len,
# 其中一个有默认值，即80，因此它必然属于最后一个参数，即max_len
# 这里使用inspect模块来处理



# 示例  5.17   提取函数的签名 （命令行模式）

# 这样就好多了，inspect.signature函数返回一个inspect.Signature对象，它有一个parameters属性，这是一个有序映射，把参数名和inspect.Parameter
# 对象对应起来。各个Parameter属性也有自己的属性，例如，name,default,kind,特殊的inspect._empty值表示没有默认值，考虑到None是有效的默认值

# kind属性的值是_ParameterKind类中的5个值之一，如下

# 1. POSITIONAL_OR_KEYWORD
# 可以通过定位参数和关键字参数传入的形参(多数python 函数的参数属于此类)
# 2. VAR_POSITIONAL  定位参数元组

# 3. VAR_KEYWORD   关键字参数
# 4. KEYWORD_ONLY   仅限关键字参数(Python3新增)
# 5. POSITIONAL_ONLY
#  仅限定位参数；目前，python声明函数的句法不支持，但是有些使用C语言实现且不接受关键字参数的函数(如divmod)支持

# 除了name,defalut和kind,inspect.Parameter对象还有一个annotation(注解)属性，它的值通常是inspect._empty,但是可能包含Python3新的注解句法
# 提供的函数签名元数据
# inspect.Signature对象有一个bind方法，它可以把任意个参数绑定到签名中的形参上，所用的规则与实参到形参的匹配方式意义。框架
# 可以使用这个方法在真正调用函数前验证参数。
# 示例5.18 把tag函数的签名绑定到一个参数字典上
# 这个示例在inspect模块的帮助下，展示了python数据模型把实参绑定给函数调用中的形参的机制，这与解释器使用的机制相同
# 框架和IDE等工具使用这些信息验证代码。python3的另一个特性————函数注解————增进了这些信息的用途