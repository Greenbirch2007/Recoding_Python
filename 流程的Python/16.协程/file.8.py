#  １６．８　　yield from 的意义

#  把迭代器当做生成器使用，相当于把子生成器的定义体内联在yielf from 表达式中，此外，子生成器可以执行return 语句，返回一个值，而返回的值会成为yield from 表达式的值


#  １．　子生成器产出的值都直接传给委派生成器的调用方(即客户端代码)
#  ２．　使用send()方法发给委派生成器的值都直接传给子生成器．如果发送的值是None，那么会调用子生成器的__next__()方法．如果发送的值不是None,
#  那么会调用子生成器的send()方法．如果调用的方法抛出StopIteration异常，那么委派生成器恢复运行．任何其他异常都会向上冒泡，传给委派生成器
#  ３．生成器退出时，生成器(或子生成器)中的return expr表达式会触发StopIteration(expr)异常抛出

#  ４．　yield from 表达式的值是子生成器终止时传给StopIteration异常的第一个参数

#  yield from 结构的另外两个特性与异常和终止有关

#  １．　传入委派生成器的异常，除了GeneratorExit之外都传给子生成器的throw()方法．
#  ２．　如果把GeneratorExit异常传入委派生成器，或在委派生成器上调用close()方法

