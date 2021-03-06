#  15.2   上下文管理器和with块

#  上下文管理器对象存在的目的是管理with语句,就像迭代器的存在是为了管理for语句一样.  与函数和模块不同,with块没有定义新的作用域

#  with语句的目的是简化try/finanlly模式.这种模式用于保证一段代码运行完毕后执行某项操作,即便那段代码由于异常,return语句或sys.exit()调用
#  而中止,也会执行指定的操作.finanlly子句中的diam通常用于释放重要额资源,或还原临时变更的状态


#  上下文管理器协议包含__enter__和__exit__两个方法.with语句开始运行时,会在上下文管理器对象上调用__enter__方法,with语句运行结束后,会在
#  上下文管理器对象上调用__exit__方法,以此扮演finanlly子句的角色

#  最常见的例子是确保关闭文件对象,使用with语句关闭文件的例子如下

#  示例15-1   演示把文件对象当成上下文管理器使用

with open('em.py') as fp:
    src = fp.read(60)


print(len(src))
print(fp)
print(fp.closed,fp.encoding)


# 执行with后面的表达式得到的结果是上下文管理器对象,不过,把值绑定到目标变量上(as子句)是上下文管理器对象上调用__enter__方法的结果

#  open()函数返回TextIOWrapper类的实例,而该实例的__enter__()方法返回self.不过,__enter__方法除了返回上下文管理器之外,还可能返回其他对象

#  不管控制流程以哪种方式退出with块,都会在上下文管理器对象上调用__exit__方法,而不是__enter__方法返回的对象上调用

#  with语句的as子句是可选的.对open函数来说,必须加上as子句,以便获取文件的引用.不过,有些上下文管理器会返回None,因为没有什么有用的对象能够共给用户
#  一个上下文管理器执行操作,以此强调上下文管理器与__enter__方法返回的对象之间的区别