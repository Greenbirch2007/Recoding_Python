# ８．１４　　实现自定义的容器
# ８．１４．１　　问题
# 我们想要实现一个自定义的类，用来模仿普通的内建容器类型比如列表或字典的行为。但是，我们并不完全确定需要实现什么方法来完成
# ８．１４．２　解决方案
# collections库中定义了各种各样的抽象基类，当实现自定义的容器类时它们会非常有用。假设我们希望自己的类能够支持迭代操作。
# 只要简单地从collections.Iterable中继承的好处就是确保必须实现所有所需的特殊方法。如果不这么做，那么在实例化时就会得到错误信息

# 要修正这个错误，只要在类中实现所需的__iter__()方法即可

# 在collections库中还有一些值得一提的类，包括Sequence,MutableSequence,Mapping,MutableMapping,Set以及MutableSet/
# 这些类中有许多是按照功能层次的递增来进行的。只要简单地对这些类进行实例化操作，就可以知道需要实现哪些方法才能让自定义的
# 容器具有相同的行为
# 下面，我们在自定义类中实现了所需的放阿飞，创建一个Sequence类，且元素总是以排序后的顺序进行存储的

import collections
import bisect

class SortedItems(collections.MutableSequence):
    def __init__(self,initial=None):
        self._items = sorted(initial) if initial is not None else []

    # required sequence methods

    def __getitem__(self, item):
        print('Getting:',item)
        return self._items[item]

    def __setitem__(self, key, value):
        print('Setting:',key,value)
        self._items[key] = value


    def __delitem__(self, key):
        print('Deleting:',key)
        del self._items[key]

    def insert(self,index,value):
        print('Inserting:',index,value)
        self._items.insert(index,value)




    def __len__(self):
        print('Len')
        return len(self._items)

    # method for adding an item in the right location

    def add(self,item):
        bisect.insort(self._items,item)

# items = SortedItems([5,1,3])
# print(list(items))
# print(items[0])
# print(items[-1])
# items.add(98)
# print(items[-1])


# SortedItems的实例所表现出的行为和一个普通的序列对象完全一样，并且支持所有常见的操作，包括索引，迭代，len(),是否包含(in操作符)甚至是切片
# 本节中用到的bisect模块能够方法吧的让列表中的元素保持有序。bisect.insort()函数能够将元素插入到里诶保重且让列表仍然保持有序

# 8.14.3  讨论
# 从collections库中提供的抽象基类继承，可确保我们的自定义容器实现了所有所需的方法。但是，这种继承也便于我们做类型检查

# items = SortedItems()
# import collections
# print(isinstance(items,collections.Iterable))
# print(isinstance(items,collections.Sequence))
# print(isinstance(items,collections.Container))
# print(isinstance(items,collections.Sized))
# print(isinstance(items,collections.Mapping))



# collections模块中的需要抽象基类还针对常见的容器方法提供了默认实现。为了说明，　假设有一个类从collections.MutableSequence中继承而来


# 如果创建一个Item实例，就会发现它几乎支持列表所有的核心方法(例如，append(),remove(),count()等)。这些方法在实现的时候只使用了所需要的那些特殊方法。

a = SortedItems([1,2,3])
print(len(a))
print(a.append(6))
print(a.append(2))
print(a.count(2))
print(a.remove(3))

# 本节只对Python的抽象类功能做了简单的介绍。numbers模块中提供了与数值数据类型相关的类似的抽象基类。

