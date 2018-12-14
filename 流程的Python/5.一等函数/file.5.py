# 5.5  用户定义的可调用类型

# 不仅python函数是真正的对象，任何Python对象都可以表现的像函数。为此，只需实现实例方法__call__

# 下面是BingoCage类。这个类的实例使用任何可迭代的对象构建，而且会在内部存储一个随机顺序排列的列表。调用实例会取出一个元素

# 示例５．８　　　bingocall.py  调用BingoCage实例，从打乱的列表中取出一个元素



import random


class BingoCage:
    def __init__(self,items):
        self._items = list(items)
        random.shuffle(self._items)


    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self, *args, **kwargs):
        return self.pick()


# 下面是示例５．８中定义的类的简单演示。注意，bingo实例可以作为函数调用，而且内置的callable(...)函数判定它是可调用的对象：


bingo = BingoCage(range(3))
print(bingo.pick())
print(bingo)
print(bingo())
print(callable(bingo))

# 实现__call__方法的类是创建函数类对象的简便方式，此时必须在内部维护一个状态，让它在调用之间可用，例如BingoCage中的剩余元素。
# 装饰器就是这样。装饰器必须是函数，而且有时要在多次调用之间"记住"某些事情[例如备忘(memoization),即缓存消耗大的计算结果，供后面使用]

# 下面讨论把函数视为对象处理的另一方面：运行时内省