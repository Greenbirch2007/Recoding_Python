#  　第２章　　序列构成的数组


# python风格:序列的泛型操作,内置的元组和映射类型,用缩进来架构的源码,无需变量声明的强类型等

#  序列都有的特征: 迭代,切片,排序,还有拼接

#  2.1  内置序列类型概览

#  python标准库用C实现了丰富的序列类型

#  1. 容器序列

#  list,tuple,collection.deque这些序列能存放不同类型的数据

#  2. 扁平序列

#  str,bytes,bytearray, memoryview和array.array,这类序列只能容纳一种类型

#  容器序列存放的是它们所包含的任意类型的对象的引用.而扁平序列里存放的是值而不是引用.扁平序列其实是一段连续的内存空间.由此可见扁平序列其实
#  更加紧凑,但是它里面只能存放诸如字符,字节和数值这种基础类型


#  序列类型还能按照能否修改来分类

#  1. 可变序列

#  list,bytearray,array.array, collections.deque和memoryview

#  2. 不可变序列

#  tuple,str,bytes

#  可变序列(MultableSequence) 和不可变序列(Sequence)的差异,同时也能看出前者从后者那里继承了一些方法.虽然内置的序列类型并不是从
#  Sequence和MulableSequence这两个抽象基类(Abstract Base Class,ABC)继承而来的


#  通过记住这些类的共有特性,把可变与不变序列或容器与扁平序列的概念融会贯通,在探索并学习新的序列类型时,

#  最重要也是最基础的序列类型就是列表(list),list是一个可变序列,并且能够同事存放不同类型的元素,
#  列表推导( list comprehension).列表推导是一个构建列表的方法.掌握列表推导还可以了解生成器表达式(generator expression),具有
#  生成各种类型的元素并用它们来填充序列的功能


