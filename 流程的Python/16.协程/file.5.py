#　１６．５　终止协程和异常处理

#预激协程中未处理的异常会向上冒泡，传给next函数或send方法的调用方(即处罚协程的对象)
# 示例１６－７　　未处理的异常会导致协程终止

# 1. 使用@coroutine装饰器装饰的averager协程，可以立刻开始发送值
# 2. 发送的值不是数字，导致协程内部有异常抛出
# 3. 由于在协程内没有处理异常，协程会终止．如果试图重新激活协程，会抛出StopIteration异常

# 客户代码可以在生成器对象上调用两个方法，显示的把异常发给协程．　这两个方法是throw和close

#  1. generator.throw(exc_type[,exc_value[,traceback]])

# 致使生成器在暂停的yield表达式处抛出指定的异常．如果生成器处理了抛出的异常，代码会向前执行到下一个yield表达式，而产出的值会成为调用generator.throw
# 方法得到的返回值.如果生成器没有抛出的异常,异常会向上冒泡,传到调用方的上下文中

#  2. generator.close()

#  致使生成器在暂停的yield表达式处抛出GeneratorExit异常,如果生成器没有处理这个异常,或抛出了StopIteration异常(通常是指运行到结尾),调用方
#　不会报错．如果接收到GeneratorExit异常，生成器一定不能产出值，否则解释器会抛出RuntimeError异常．生成器抛出的其他异常会向上冒泡，传给调用方

#　示例１６－８　　学习在协程中处理异常的测试代码

class DemoException(Exception):
    '''为了这次演示定义的异常类型'''

def demo_exc_handling():
    print('-> coroutine started')
    while True:
        try:
            x = yield
        except DemoException:
            print('*** DemoException handled.Continuing...')
        else:
            print('-> coroutine received"{!r}'.format(x))
    raise RuntimeError ('This line should never run.')

# 1.特别处理DemoException异常　２．　如果没有异常，那么显示接收到的值　

