#  １．３　　特殊方法一览



#  如下跟运算符无挂你的特殊方法

#  １．　字符串／字节序列／表示形式　　　　　__repr__,__str__, __format__,__bytes__

#  2.数值类型　　 __abs__,__bool__, __complex__, __init__, __float__,__hash__,__index__

#  3. 集合模拟　　　__len__,__getitem__, __setitem__,  __delitem__, __contains__

#  4. 迭代枚举　　　　__iter__,  __reversed__,__next__

#  5. 可调用模拟　　　__call__
#  6. 上下文管理　　__enter__,  __exit__
#  7. 实例创建和销毁　　__new__, __init__, __del__

#  8. 属性管理　　　__getattr__, __getattribute__,  __setattr__,__delattr__, __dir__

#  9. 属性描述符　　__get__,  __set__, __delete__

#  10. 跟类相关的服务　　__prepare__,__instancecheck__,  __subclasscheck__


#   　跟运算符相关的特殊方法

#  １．　一元运算符　　　__neg__ -, __pos__ + ,  __abs__ abs()
#  2.  众多比较运算符　　　__lt__ < , __le__ <= , __eq__ ==, __ne__ !=  __gt__ > ,  __ge__ >=
#  3. 算术运算符　　__add__ + ,  __sub__ - ,  __mul__ * , __truediv__ / , __floordiv__ //
#    __mod__ % , __divmod__ divmod(),  __pow__ **或pow(), __round__, round()

#  4. 反向算术运算符　　__radd__, _rsub__,__rmul__,__rtruediv__,__rfloordiv__, __rmod__,__rdivmod__, __rpow__

#  5. 增量赋值算术运算符　　　__iadd__,__isub__,__imul__,  __itruediv__,__ifloordiv__,__imod__,__ipow__
#  6. 位运算符　　　__invert__ ~ , __lshift__ << , __rshift__ >> , __and__ & , __or__ |  , __xor__ ^

#  7. 反向位运算符　　　__rlshift__,__rrshift__,__rand__,__rxor__,__ror__
#  8. 增量赋值位运算符　__ilshift__,irshift__, __iand__, __ixor__,

#  当交换两个操作数的位置时，就会调用反向运算符(b*a而不是a*b)．增量赋值运算符则是一种把中辍运算符变成赋值运算的捷径(a= a*b就变成了a *=b)

#  1.5 本章小节

#  python 对象的一个基本要求就是它得有合理的字符串表示形式，我们可以通过__repr__和__str__来满足这个要求．前者方便我们调试和记录日志，后者则是给终端用户看的．
#  这就数据模型中存在特殊方法__repr__和__str__的原因

