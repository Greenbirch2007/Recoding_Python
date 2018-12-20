#　2.6 序列的增量父子

#　+= 背后的特殊方法是__iadd__(就地加法) .一般来说,可变序列一般都实现了__iadd__方法,而不可变序列根本就不支持这个操作
#　*=  对应的是__imul__魔法方法

#　对于不可变序列进行重复拼接操作的化,效率会很低,因为每次都有一个新对象,而解释器需要把原来对象中的元素先复制到新的对象里,然后再追加新的元素

#　一个关于 += 的谜题

#　str是一个例外，因为对字符串做+=实在太普遍了，所以CPython对它做了优化，为str初始化内在的时候，程序会为它留出额外的可扩展空间，因此进行增量操作的时候，并不会
#　设计赋值原有字符串到新位置这类操作

#　不要把可变对象放在元组里面
#　增量赋值不是一个原子操作．
#　查看python的字节码并不难，

#　下面关注*,+ 对于序列类型的一个方面：排序