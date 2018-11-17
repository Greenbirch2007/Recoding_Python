# 第１０章　模块和包

# 模块和包是任何大型项目的核心，就连Python安装程序本身就是一个包。本章涉及，如何组织包，将大型的模块分解为多个文件
# 以及创建命名空间包(namespace package)

# 10.1  把模块按层次结构组织成包

# 10.1.1 问题
# 我们想把代码按照一定的层次结构组织成包
# 10.1.2  解决方案
# 10.1.3 讨论
# 定义一个具有层次结构的模块就如同在文件系统上常见目录结构一样简单。__init__.py文件的目的就是包含可选的初始化代码，当遇到软件包中不同层次
# 的模块时会触发运行。比如，

#   import graphics语句 ——————————> 文件graphics/__init__.py会被导入并形成graphics命名空间的内容
#  import grahics.formats.jpg ——————————> 文件graphics/__init__.py 和 graphics/formats/__init__.py都会在最终导入文件grahics.formats.jpg之前优先先得到导入
# 在大部分情况下，把__init__.py文件留空也是可以的。但是，在某些特定的情况下___init__.py文件中是需要包含代码的。
# 例如，可以用__init__.py文件来自动加载于模块。如下


# graphics/formats/__init__.py

from . import jpg
from . import png

# 有了这样一个文件，用户只需要使用一条单独的 import graphics.formats 语句就可以导入jpg,png模块了，不需要再去分别导入graphics.formats.jpg和graphics.formats.png

# 关于__init__.py文件的常见用法包括从多个文件中把定义统一到一个单独的逻辑命名空间中，这有时候会在分解模块是用到


