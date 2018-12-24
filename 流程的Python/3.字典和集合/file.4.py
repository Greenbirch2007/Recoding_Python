#  3.4  映射的弹性键查询

#  为了方便期间,就算某个键在映射里不存在,我们也希望在通过这个键读取值的时候能够得到以一个默认值.有两个途径能帮我们达到这个目的
#  一个是通过defaultdict这个类型而不是普通的dict,另一个是给自己定义一个dict的子类,然后在子类中实现__missing__方法


#  3.4.1  defaultdict:处理找不到的键的一个选择

#  在用户创建defaultdict对象的时候有,就需要给它配置一个为找不到的键创造默认值的方法

#  具体,在实例化一个defaultdict的时候,需要给构造方法提供一个可调用对象,这个可调用对象会在__getitem__碰到找不到的键的时候被调用,
#  让__getitem__返回某种默认值


#  比如,我们新建了一个字典:dd = defaultdict(list),如果键'new-key'在dd中还不存在的化,表达式dd['new-key']会按照以下步骤来处理:

#  (1) 调用 list()来建立一个新列表
#  (2) 把这个新列表作为值,'new-key'作为它的键,放到dd中
#  (3) 返回这个列表的引用

#  而这个用来生成默认值的可调用对象存放在名为default-factory的实例属性里

#  __missing__会在defaultdict遇到找不到的键的时候调用default_factory,而实际上这个特性是所有映射类型都可以选择去支持的

#  3.4.2   特殊方法__missing__

#  所有的映射类型在处理找不到的键的时候,都会牵扯到__missing__方法.如果有一个类继承了dict,然后这个继承类提供了__missing__方法,
#  那么在__getitem__碰到找不到键的时候,Python就会自动调用它,而不是抛出一个KeyError


#  __missing__方法只会被__getitem__调用(比如在表达式d[k]中).提供__missing__方法对get或__contains__(in 运算符会用到这个方法)
#  这些方法的时候没有影响

#  如果要自定义一个映射类型,更适合的策略是继承collections.UserDict类

#　示例３－７　　SKD类在查询的时候把非字符串的键转换为字符串

class SKD(dict):

    def __missing__(self, key):
        if isinstance(key,str):
            raise KeyError(key)
        return self[str(key)]

    def get(self,key,default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()


