# 7.8 标准库中的装饰器

# python内置了三个用户装饰方法的函数：property,classmethod,staticmethod
#　另外一个常见的装饰器是functools.wraps。它的作用是协助构建行为良好的装饰器。标准库中最值得关注的两个装饰器是lru_cache和全新的singledspath
# 这两个装饰器都在functools模块中定义.

#　7.8.1 使用functools.lru_cache做备忘

#functools.lru_cache是非常实用的装饰器，它实现了备忘(memoization)功能。装饰一项优化技术，它把耗时的保存起来，避免传入相同的参数时重复计算，LRU
# 表示缓存不会无限制增长，一段时间不用的缓存条目会被扔掉

# 生成第n个斐波那契书这种慢速递归函数适合使用lru_cache

# 示例７．１８　　生成第n个斐波那契数，

# 使用lru_cache,性能会显著提高
# 示例7.19   使用缓存实现，速度更快

import  functools


from clockdeco import clock


# @functools.lru_cache()
# @clock
# def fiboacci(n):
#     if n <2:
#         return n
#     return fiboacci(n-2)  + fiboacci(n-1)
#
#
# if __name__ == '__main__':
#     print(fiboacci(6))

# 注意@functools.lru_cache(),是必须加括号的，因为lru_cache可以接受配置参数
#　叠放装饰器，@lru_cache()应用到＠clock返回的函数上

# 除了优化地柜算法职位，lru_cache在从web中获取信息的应用也能发挥巨大作用。lru_cache可以使用两个参数来配置，如
functools.lru_cache(maxsize=128,typed=False)
# 其中maxsize参数制定存储多个调用的结果，缓存满了之后，旧的结果会被扔掉，腾出空间为了得到最佳性能，maxsize应该是2的幂、
#　typed参数如果设为True，把不同的参数类型得到的结果分开保存，即把通常认为相等的浮点数和整数参数(如１,1.0)区分开。
# 因为lru_cache使用字典存储结果，而且键根据调用时传入的定位参数和关键字参数创建，所以被lru_cache装饰的函数，它的所有参数都必须是可散列的
#  下面是functools.singleddispatch装饰器
# 7.8.2  单分派泛函数

#  假设我们在开发一个调试web应用的工具，想生成html，显示不同类型的python对象

import html

def htmlsize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)



# 和这个函数适用任何python类型，这里做了扩展，让它适用特别的方法类型

# str：把内部的换行符替换为'<br>/n'; 不使用<pre>,而是适用<p>
# int:以十进制和十六机制显示数字
#　list:输出一个html列表，根据哥哥元素的类型进行格式化

#  示例 7.20   生成html的htmlsize函数，调整了几种对象的输出

print(htmlsize({1,2,3}))