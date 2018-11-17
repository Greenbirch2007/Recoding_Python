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

# 下面的解决方案正是应对于此，我们使用了元类以及描述符来实现

# multiple.py

import inspect
import types

class MultiMethod:
    '''Represents a single multimehod
    '''
    def __init__(self,name):
        self._methods = {}
        self.__name__ = name

    def register(self,meth):
        '''Register a new method as a multimethod'''
        sig = inspect.signature(meth)
        # build a type signature from the method's annotations
        types = []
        for name,parm in sig.parameters.items():
            if name == 'self':
                continue
            if parm.annotation is inspect.Parameter.empty:
                raise TypeError (
                    'Argument {} must be annotated with a type'.format(name)
                )

            if not isinstance(parm.annotation,type):
                raise TypeError(
                    'Argument {} annotation must be a type'.format(name)
                )
            if parm.default is not inspect.Parameter.empty:
                self._methods[tuple(types)]  = meth
            types.append(parm.annotation)

        self._methods[tuple(types)] = meth

    def __call__(self, *args):
        '''Call a method based on type sigature of the arguments'''
        types = tuple(type(arg) for arg in args[1:])
        meth = self._methods.get(types,None)
        if meth:
            return meth(*args)
        else:
            raise TypeError('No matching method for types {}'.format(types))

    def __get__(self, instance, cls):
        '''Descriptor method needed to make calls work in a class'''
        if instance is not None:
            return types.MethodType(self,instance)
        else:
            return self

class MultiDict(dict):
    '''Special dictionary to build multimethods in a metaclass'''
    def __setitem__(self, key, value):
        if key in self:
            # if key already exists,it must be a multimethod or callable
            current_value = self[key]
            if isinstance(current_value,MultiMethod):
                current_value.register(value)
            else:
                mvalue = MultiMethod(key)
                mvalue.register(current_value)
                mvalue.register(value)
                super().__setitem__(key,mvalue)
        else:
            super().__setitem__(key,value)

class MultipleMeta(type):
    '''Metaclass that allows multiple dispatch of methods'''
    def __new__(cls, clsname,bases,clsdict):
        return type.__new__(cls,clsname,bases,dict(clsdict))

    @classmethod
    def __prepare__(cls, clsname, bases):
        return MultiDict()


# 要使用这个类，可以如下

class Spam(metaclass=MultipleMeta):
    def bar(self,x:int,y:int):
        print('Bar 1:',x,y)

    def bar(self,s:str,n:int=0):
        print('Bar 2:',s,n)

# example：over loaded __init__

import time
class Date(metaclass=MultipleMeta):
    def __init__(self,year:int,month:int,day:int):
        self.year = year
        self.month = month
        self.day = day

    def __init__(self):
        t = time.localtime()
        self.__init__(t.tm_year,t.tm_mon,t.tm_mday)


s = Spam()
s.bar(2,3)

d = Date(2012.12,21)

# 9.20.3 讨论
# 本节中出现了大量的"魔法方法"才使得方案是用于现实环境中的
# 元类Mutiple使用__prepare__()方法提供一个定制化的类字典，将其作为MultiDict的一个实例。与普通的字典不同，当设定字典的条目
# 时，MultiDict会检查条目是否已经存在。如果应景存在，则重复的条目会被合并到ＭultiMethod的一个类实例中去

#