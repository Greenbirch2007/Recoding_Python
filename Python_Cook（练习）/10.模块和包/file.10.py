# 10.10  使用字符串中给定的名称来导入模块
# １０．１０．１　　问题
# 我们已经有了需要导入的模块名称，但是这个名称保存在一个字符串里。我们想在字符串上执行import命令
# １０．１０．２　解决方案
# 当模块或包的名称以字符串的形式给出时，可以使用importlib.import_module()函数来手动导入这个模块如下

# import importlib
#
# mat = importlib.import_module('math')
# print(mat.sin(2))
#
#
# mod  = importlib.import_module('urllib.request')
# html = mod.urlopen('http://www.python.org')
# print(html)


# import_module基本上和import完成的步骤相同，但是import_module会把模块对象作为结果返回给你。我们只需要将它保存在一个变量里，之后
# 把它当做普通的模块使用即可
# 如果要同包打交道，import_module()也可以用来实现相对导入。但是，需要提供一个额外的参数，如下

import importlib

# same as 'from . import b'
b = importlib.import_module('.b',__package__)
# 10.10.3 讨论
# 　采用　import_module()手动导入模块的需求最常出现在当编写代码以某种方式来操作或包装模块时。例如，约需正在实现一个自定义的导入机制，需要
# 通过模块的名称来完成加载并加载及你来的代码打上补丁

# 在较老的代码中，有时候会看到内建的__import__()函数来实现导入。尽管这样也行得通，但是import.import_module()通常要更容易一些
