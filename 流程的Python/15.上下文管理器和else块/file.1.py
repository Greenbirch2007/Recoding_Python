#  第15章  上下文管理器和else块


#  本章会讨论

#  1. with语句和上下文管理器   2.  for,while,try语句的else子句

#  with语句会设置一个临时的上下文,交给上下文管理器对象控制,并且负责清理上下文.这么做能够避免错误并减少样板代码.因此api更安全,而且更易于
#  使用.除了自动关闭文件之外,with块还有很多用的

#  else子句与with语句完全没有关系.

#  15.1  先做这个,再做这个: if语句之外的else块

#  else子句不仅能在if语句中使用,还能在for,while,try语句中使用

#  else子句的行为如下:

#  1. for   仅当for循环运行完毕时(即for循环没有被break语句中止) 才运行else块

#  2. while  仅当while循环因为条件为假值而退出时(即while循环没有被break语句中止)才运行else块

#  3.  try  仅当try块中没有异常抛出时才运行else块


#  在所有情况下,如果异常或return,break,或continue语句导致控制全跳到了复合语句的主块之外,else子句也会被跳过

#  if语句之外,在其他语句选择使用else关键字是个错误,因为else隐含着"排他性"

#  在这些语句中使用else子句通常让代码更易于阅读.不用设置控制标志或添加额外的if语句.
#  在循环中使用else子句的方式如下

for item in mylist:
    if item.flavor == 'banana':
        break
    else:
        raise ValueError('No banana flaovr found!')

# 在python中,try/except不仅用于处理错误,还常用于控制流程.