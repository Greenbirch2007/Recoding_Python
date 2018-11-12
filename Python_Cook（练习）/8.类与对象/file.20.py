# 8.20  调用对象上的方法，方法名以字符串形式给出
# 8.20.1 问题
#  我们想调用对象上的某个方法，现在这个方法名保存在字符串中，我们想通过它来调用该方法
#  8.20.2 解决方案
#  对于简单的情况，可能会使用getattr()

import math


#  另一种方法使用operator.methodcaller()

#  如果向通过名称来查询方法并提供同样的参数反复调用该方法，那么operaor.methodcaller()是很有用的


#  8.20.3 讨论

# 调用一个方法实际上设计两个单独的步骤：1.一是查询属性，2.而是函数调用。因此，要调用一个方法，可以使用getattr()来查询相应的属性。
# 要调用查询到的方法，只要把查询的结果当做函数即可

# operator.methodcaller()创建了一个可调用对象，而且把所需的参数提供给了被调用的方法。我们所要做的就是提供恰当的self参数即可



# 通过包含在字符串中的名称来调用方法，这种方式时常出现在需要模拟case语句或访问者模式的变体中。