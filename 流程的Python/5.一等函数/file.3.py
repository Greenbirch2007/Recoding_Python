# 匿名函数

# lambda关键字在python表达式内创建匿名函数
# 然而，python简单句法限制了lambda函数的定义体只能使用纯表达式，lambda函数的定义体不能赋值，也不能使用while和try等语句

# 在参数列表中最适合使用匿名函数。
# 示例５．７　　使用lambda表达式反转拼写，然后一次给单词列表排序


fruits = ['strawberry','fig','apple','cherry','raspberry','banana']
print(sorted(fruits,key=lambda word:word[::-1]))

# 除非作为参数传给高阶函数职位，python很少使用匿名函数

# lambda句法只是语法糖：与def语句一样，lambda表达式会创建函数对象。　这是一种可调用对象
