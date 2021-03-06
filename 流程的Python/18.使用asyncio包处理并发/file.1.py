#  第18 章 使用asyncio包处理并发

#  并发是一次处理多件事,并行是指一次做多件事,一个关于结构,一个关于执行.并发用于指定方案,用来解决可能(但未必)并行的问题

# 本章主要讨论
# 摒弃线程或进程,如何使用异步编程管理网络应用中的高并发
# 在异步编程中,与回调对比,协程显著提升性能的方式
# 如何把阻塞的操作交给线程池处理,从而避免阻塞事件循环
# 使用asynico编写服务器,重新审视web应用对高并发的处理方式

# 18.1  线程与协程对比

# 使用@asynico.coroutine装饰器代替线程
# 打算交给asyncio处理的协程要使用@asynico.coroutine装饰
# 除非想阻塞主线程,从而冻结事件循环或整个应用,否则不要在asyncio协程中使用time.sleep()如果协程需要一段时间内什么都不做,应该使用yield from asynico.sleep(DELAY)

# 18.1.1  asyncio.Future :故意不阻塞

# 18.2  使用asyncio和aiohttp包下载

# 18.3 避免阻塞型调用


# 18.6  使用asyncio包编写服务器