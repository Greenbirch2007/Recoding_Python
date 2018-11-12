# 8.23 在环形数据结构中管理内存
# 8.23.1 问题
# 我们的程序中创建了环状的数据结构(如，树，图，观察者模式等)，但是在内存管理上却遇到麻烦

# 8.23.2 解决方案
# 环状数据结构的一个简单例子就是树，这里父节点指定它的孩子，而子节点又会指回它们的福界定啊。我们应该考虑让其中一条连接使用weakref库
# 中提供的弱引用机制



import weakref

class Node:
    def __init__(self,value):
        self.value = value
        self._parent  = None
        self.children = []

    def __repr__(self):
        return 'Node({!r:})'.format(self.value)

    # property that manages the parent as a weak-reference

    @property
    def parent(self):
        return self._parent if self._parent is None else self._parent()

    @parent.setter
    def parent(self,node):
        self._parent = weakref.ref(node)

    def add_child(self,child):
        self.children.append(child)
        child.parent = self

root = Node('parent')
c1 = Node('child')
root.add_child(c1)
print(c1.parent)
print(c1.children)


# 8.23.3 讨论
# 环形数据结构是Python中较难理解的部分，因为普通的垃圾收集规则并不适用于环状数据结构

# Python的垃圾收集器是基于简单地引用计数规则来实现的。当对象的引用计数为0时就会被立刻删除掉。而对于环状数据结构来说这绝对不可能发生。
# 因为在最后那种情况下，由于父节点和子节点互相引用对象，引用计数不会为0

# 要处理环状数据结构，还有一个单独的垃圾收集器会定期运行。但是，一般来说我们不知道它会在何时运行。因此，没法知道环状数据结构具体会在何时被回收。
# 如果有必要的话，可以强制运行垃圾收集器，但这么做会相对于全自动的垃圾收集有些被捉

# 内存泄露。弱引用通过消除循环引用来解决内存泄露。本质上说，弱引用就是一个指向对象的指针，但是不会增加对象本身的引用计数。
# 可以通过weakref库来创建弱引用

# 要提领(dereference)一个弱引用，