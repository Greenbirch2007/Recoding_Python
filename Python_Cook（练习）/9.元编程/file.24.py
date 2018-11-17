# 9.24  解析并分析Python  源代码

#9.24.1  问题

# 我们想编写程序来解析Python源代码并对此进行一些分析工作

# ９．２４．２　　解决方案
# Python可以执行以字符串形式提供的源代码

x = 42
eval('2+3*4 + x')
# exec('for i in range(10):print(i)')
# 我们可以使用ast模块将Python源代码编译为一个抽象语法树(AST)这样可以分析源代码


import ast

ex = ast.parse('2+3*4 +x',mode='eval')
print(ex)
print(ast.dump(ex))