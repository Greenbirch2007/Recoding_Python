#  ３．７　　不可变映射理性

#  从python3.6开始，types模块中引入了一个封装类名为MappingProxyType.如果给这个类一个映射，它会返回一个只读的映射视图．虽然是一个只读视图
#  但是它是动态的．这意味着如果对原映射做出了改动，我们通过这个视图可以观察到，但是无法通过这个视图对原映射做出修改


#  示例３－９　　用MappingProxyType来获取字典的只读实例mappingproxy


from types import MappingProxyType

d = {1:'a'}
d_proxy = MappingProxyType(d)
print(d_proxy)
d[2]='b'
print(d_proxy)
