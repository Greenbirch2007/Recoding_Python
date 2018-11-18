

#批量创建文件夹
import os

# themes = ['Python3面向对象编程','Python高级编程2th','Python 核心编程2th','流程的Python','Python参考手册4th']
themes = ['１．python数据模型','2.序列构成的数组','3.字典和集合','4.文本和字节序列','5.一等函数','6.使用一等函数实现设计模式','7.函数装饰器和闭包','8.对象引用，可变性和垃圾回收','９．符合python风格的对象','10.序列的修改，散列和切片','11.接口：从协议到抽象基类','12.继承的优缺点','13.正确重载运算符','14.可迭代的对象，迭代器和生成器','15.上下文管理器和else块','16.协程','17.使用期物处理并发','18.使用asyncio包处理并发','19.动态属性和特性','20.属性描述符','21.类元编程']
base = "/home/karson/Recoding_Python/流程的Python/"
for i in themes:
    file_name = base + str(i)
    os.mkdir(file_name)


