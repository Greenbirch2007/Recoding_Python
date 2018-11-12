# 8.19 实现带有状态的对象或状态机

# 8.19.1  问题
# 我们想实现一个状态机，或让对象可以在不同的状态中进行操作。但是我们并不希望代码里会因此出现大量的条件判断
# 8.19.2  解决方案
# 在某些应用程序中，我们可能会让对象根据某种内部状态来进行不同的操作，如下，考虑这个diam网络链接的类

# 8.19.3 讨论

# 编写含有大量复杂的条件判断并和各种状态纠缠在一起的代码难以维护和解读。通过各个状态分解为单独的类来避免这个问题
# 在每种状态都用类和静态方法来实现，在每个静态方法中都把Connection类的实例作为第一个参数。产生这种设计的原因在于
# 我们决定在不同的状态类中不保存任何实例数据。相反，所有的实例数据应该保存在Connection实例中。将所有的状态放在一个公共的
# 基类下，这么做的大部分原因是为了帮助组织代码，并确保适当的方法得到实现。


#  另一种方法是考虑直接修改实例的__class__属性