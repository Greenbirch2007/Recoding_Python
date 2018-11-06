# 让带有N个参数的可调用对象以较少的参数形式调用

# 7.8.1  问题
# 我们有一个可调用对象可能会以回调函数的形式同其他的的Python代码交互。但是这个可调用对象需要的参数过多
# 如果直接调用会发生异常



# 7.8.2  解决方案
# 如果需要减少函数的参数数量，应该使用functools.partial().函数partial()允许我们给一个或多个参数指定固定的值，
# 以此减少需要提供给之后的参数数量。为了说明这个过程，假设有这么一个函数：

def spam(a,b,c,d):
    print(a,b,c,d)

# 现在考虑用partial()来对参数赋固定的值：

from functools import partial

s1 = partial(spam,1)
s1(2,3,4)
s1(4,5,6)
s2 = partial(spam,d=42)
s2(1,2,3)

s3 = partial(spam,1,2,d=42)
s3(66)

# 我们可以观察到partial()对特定的参数赋了固定值并返回一个全新的可调用对象。这个新的可调用对象仍然需要通过指定
# 那些未被赋值的参数来 调用。这个新的可调用对象将传递给partial()的固定参数结合起来，统一将所有的参数
# 传递给原始的函数

# 7.8.3  讨论
# 本节提到的技术对于将看似不兼容代码结合起来
# 第一个例子，假设有一列以元组(x,y)来表示的点坐标。可以用下面的函数来计算两点之间的距离

points =[(1,2),(3,4),(5,6),(7,8)]
import math

def distance(p1,p2):
    x1,y1 = p1
    x2,y2 = p2
    return math.hypot(x2-x1,y2-y1)


# 现在假设想根据这些点之间的距离来对它们排序。列表的sort()方法可接受一个key参数，它可用来做自定义的排序处理。但是它只能和接受
# 但参数的函数一起工作(因此和distance()是不兼容的)。下面我们用partial()来解决这个问题

pt = (4,3)
points.sort(key=partial(distance,pt))
print(points)

# 我们可以对这个思路进行扩展，partial()常常可用来调整其他库中的用到的回调函数的参数签名。比方说，这里有一段代码利用multiprocessing模块
# 以异步方式计算某个结果，并将这个结果传递给一个回调函数。该回调函数可接受这个结果以及一个可选的日志参数：

def output_result(result,log=None):
    if log is not None:
        log.debug("Got:%r",result)

# a sample function

def add(x,y):
    return x+y


if __name__ =="__main__":
    import logging
    from multiprocessing import Pool
    from functools import partial

    logging.basicConfig(level=logging.DEBUG)

    log = logging.getLogger('test')

    p = Pool()
    p.apply_async(add,(3,4),callback=partial(output_result,log=log))
    p.close()
    p.join()

# 当我们在apply_async()中指定回调函数时，额外的日志参数是通过partical()来指定的。multiprocessing模块对与这些
# 细节根本一无所知————它只通过单个参数来调用回调函数

# 作为类似的例子，考虑一下我们在编写网络服务器程序时面对的问题。有了socketserver模块，这一切相对
# 来说变得很简单了。比方说，羡慕有一个简单的echo服务程序：


from socketserver import StreamRequestHandler,TCPServer
#
class EchoEandle(StreamRequestHandler):
    def handle(self):
        for line in self.rfile:
            self.wfile.write(b"GOT:"+line)




# 现在，假设我们想在EchoHandler类中增加一个__init__()方法，让它接受一个额外的配置参数，示例如下


class EchoEndler(StreamRequestHandler):

    def __init__(self,*args,ack,**kwargs):
        self.ack = ack
        super().__init__(*args,**kwargs)

    def handle(self):
        for line in self.rfile:
            self.wfile.write(self.ack + line)
serv = TCPServer(("",15000),EchoEandle)
print(serv.serve_forever())

# 如果做了上述改动，现在就会发现没法简单地将其插入到TCPServer类中了。事实上，你会发现代码出现异常
# 初步看上去，除了修改socketserver的源代码或采用一些拐弯抹角的技巧外，似乎无法修改代码
#  但是，利用partical()就能轻松解决这个问题。只用partical()中提供ack的参数值即可如下

from functools import partial

serv = TCPServer(("",15000),partial(EchoEndler,ack=b'RECEIVED:'))
print(serv.serve_forever())


# 在这个例子里，__init__()方法中对参数ack的指定看起来有些疑惑，但它是以keyword-only参数的形式来指定的。

# 有时候也可以通过lambda表达式来代替partical().比如，上面这几个例子也可以采用这些语句来实现


# 但是使用partial()会使得你的意图更加明确(即为某些参数提供默认值)