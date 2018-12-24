#  字典的变种

#  １．　collections.OrderedDict
#  这个类型在添加键的时候会保持顺序，因此键的迭代次序总是一直的．




#  2.  collections.ChainMap

#  该类型可以容纳数个不同的映射对象，然后在进行键查询操作的时候，这些对象会被当做一个整体被逐个查找，直到键找到为止

#  3.  collections.Counter


#  这个映射类型会给键准备一个整数计数器．每次更新一个键的时候都会增加这个计数器．所以这个类型可以用来给可散列对象计数，或是当成多重集来用－－
#  多重集合就是集合里的元素可以出现不止一次


#  4. collections.UserDict
#  这个类其实就是把标准dict用纯python又实现了一遍

#  跟OrderedDcit,ChainMap 和Counter这些开箱即用的类型不同，UserDict是让用户继承写子类的