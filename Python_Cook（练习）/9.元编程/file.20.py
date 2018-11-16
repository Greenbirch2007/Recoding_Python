#　９．２０　通过函数注解来实现方法重载

#  9.20.1  问题
# 我们已经学习过函数参数注解方面的知识，而我们想利用这种技术通过基于参数类型的方式来实现多分派(multiple-dispatch,方法重载)。但是
# 但是并不清楚这其中要设计那些技术，甚至对于这么做是否为一个好主意还存疑

# ９．２０．２　解决方案

# 本节的思想基于一个简单的事实————即，由于Python允许对参数进行注解，那么如果可以向下面这样编写代码就好

class Spam:
    def bar1(self,x:int,y:int):
        print('Bar 1:',x,y)
    def bar2(self,s:str,n:int=0):
        print('Bar 2:',s,n)

s = Spam()
s.bar1(2,3)
s.bar2('hello')

# 下面