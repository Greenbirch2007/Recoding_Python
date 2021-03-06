#　２０．３　　方法是描述符


#　在类中定义的函数属于绑定方法(bound method),因为用户定义的函数都有__get__方法，所以依附到类上时，就相当于描述符


#　示例２０－１４　　Text类，继承自UserString类


# 绑定方法对象还有一个__call__方法，用于处理真正的调用过程．这个方法会调用__func__属性引用的原始函数，把函数的第一个参数设为绑定方法
# 的__self__属性．这就是形参self的隐式绑定方式

# 函数会变成绑定方法，这就是python语言底层使用描述符的最好例子