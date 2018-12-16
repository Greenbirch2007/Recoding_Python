# 第１７章　使用期物处理并发


# 期物是指一个对象，表示异步执行的操作
# 主要有两个模块　　１．　concurrent.futures模块　　　２．　asyncio包



# １７．１　　示例：网络下载的三种风格
# 为了高效处理网络I/O，需要使用并发，因为网络有很高的延迟，所以为了不浪费CPU周期去等待，最好在收到网络响应之前做其他的式

# １７．１．１　　依次下载的脚本


# １７．１．２　　使用concurrent.futures模块下载
# concurrent.futures模块的主要特色是ThreadPoolExecurtor和ProcessPoolExecutor类.这两个类实现的接口能分别在不同的线程或进程中执行
#　可调用的对象．这两个类在内部维护这一个工作线程或进程池，以及要执行的任务队列，不过，这个接口抽象的层级很高，像下载国旗这种简单的案例，无需关心任何实现细节

# 示例17-3  展示如何使用ThreadPoolExecutor.map方法,以最简单的方式实现并发下载


#  17.1.3 期物在哪里


#  期物是concurrent.futures模块和asyncio包的重要组件
# python3.4 开始,标准库中有两个有名的Futures的类 , concurrent.futtures.Future和asyncio.Future .这两个类的作用相同:两个Future类的实例
# 都表示可能已经完成或尚未完成的延迟计算.这与Twisted引擎中的Deferred类,Tornado框架中的Future类,以及多个javascript库中的Promise对象类似

# 期物封装待完成的操作,可以放入队列,完成的状态可以查询,得到结果(或抛出异常)后可以获取结果(或异常)
# 通常情况下自己不应该创建期物,而只能由并发框架(concurrent.futures或asyncio)实例化.原因很简单,期物表示终将发生的事情,而确定某件事情会发生的唯一
# 方式是执行的时间已经排定.因此,只有排定把某件事交给concurrent.futures.Executor子类处理时,才会创建concurrent.futures.Future实例

# 客户端代码不应该改变期物的状态,并发框架在期物表示的延迟计算结束后会改变期物的状态,而我们无法控制计算何时结束