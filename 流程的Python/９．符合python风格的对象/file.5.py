#　９．５　格式化显示

#内置的format()函数和str.format()方法把各个类型的格式化方法委托给相应的.__format__(format_spec)方法、format_spec是格式说明符

#　format(my_obj,format_spec)的第二个参数，或者
#　str.format()方法的格式字符串，{}里代换字段中冒号后面的部分
#　str.format()方法使用的{:}代换字段表示法(包含转换标志(!s,!r,!a)