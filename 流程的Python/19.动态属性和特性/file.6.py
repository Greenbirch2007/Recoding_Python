#  19.6  处理属性的重要属性和函数

#  python为处理动态属性而提供的内置函数和特殊的方法,



#  19.6 .1  影响属性处理方式的特殊属性

#  1.  __class__  对象所属类的引用(即obj.__class__与type(obj)的作用相同).python的某些特殊方法,例如__getattr__,只在对象的类中寻找,而不在实例中寻找

#  2. __dict__  一个映射,存储对象或类的可读写属性.有__dict__属性的对象,任何时候都能随意设置新属性.如果类有__slots__属性,它的实例可能没有
#  __dict__属性.

#  3. __slots__  类可以定义这个属性,限制实例能有哪些属性,__slots__属性的值是一个字符串组成的元组,指明允许有的属性.
#  如果__slots__中没有"__dict__",那么该类的实例没有__dict__属性,实例只允许有指定名称的属性


#  __slots__属性的值虽然可以是一个列表,但是最好始终使用元组,因为处理完类的定义体之后再修改__slots__列表没有任何作用,所以使用
#  可变的序列容易让人误解

#  19.6.2  处理属性的内置函数

#  下面5个内置函数对对象的属性做读,写和内省操作

#  1.dir([object])

#  列出对象的大多数属性.dir函数的目的是交互式使用,因此没有提供完整的属性列表,只列出一组"重要的"属性名,dir函数能审查有或没有__dict__属性的对象
#  dir函数不会列出__dict__属性本身,但会列出其中的键.dir函数也不会列出类的几个特殊属性,例如
#  __mro__,__bases__,__name___.如果没有指定可选的object参数,dir函数会列出当前作用域中的名称


#  2. getattr(object,name[,default])
#  从object对象中获取name字符串对应的属性.获取的属性可能来自对象所属的类或超类.如果没有指定的属性,getattr函数抛出AttributeError异常,或者
#  返回default参数的值(如果设定了这个参数的话)

#  3. hasattr(object,name)

#  如果object对象中存在指定的属性,或能以某种方式(例如继承)通过object对象获取指定的属性,返回True.这个函数的实现方法是调用getattr(object,name)函数
#  看看是否抛出AttributeError异常


#  4. setattr(object,name,value)

#  把object对象指定属性的值设为value,前提是object对象能接受的那个值.这个幻术可能会创建一个新属性,或覆盖现有的属性


#  5.vars([object])

#  返回object对象的__dict__属性,如果实例所属的类定义了__slots__属性,实例没有__dict__属性,那么vars函数不能处理那个实例(相反,dir函数能处理
#  这样的实例).如果没有指定参数,那么vars()函数的作用与locals()函数一样:返回表示本地作用域的字典


#  19.6.3  处理属性的特殊方法

#  在用户自己定义的类中,下面特殊方法用于获取,设置,删除和列出属性

#  使用点好或内置的getattr,hasattr,setattr函数存取属性都会触发下面的特殊方法,但是,直接通过实例的__dict__属性读写属性不会触发这些特殊方法---

#  如果需要,通常会使用这种方式跳过特殊方法

#  对用户自己定义的类来说,如果隐式调用特殊方法,仅当特殊方法在对象所属的类型上定义,而不是在对象的实例字典中定义时,才能确保调用成功


#  要假定特殊方法从类上获取,即便操作目标是实例.因此,特殊方法不会被同名实例属性覆盖


#  假设有个名为Class的类,obj是Class类的实例,attr是obj的属性

#  不管是使用点号存取属性.还是使用dir,getattr,hasattr,setattr,vars中的任意一个内置函数,都会出触发下面特殊方法中的一个.
#  例如,obj.attr和getattr(obj,"attr",42)都会触发Class.__getattribute__(obj,'attr')方法


#  1.   __delattr__(self,name)

#  只要使用del语句删除属性,就会调用这个方法.例如,del obj.attr语句触发Class.__delattr__(obj,'attr')方法


#  2.   __dir__(self)

#  把对象传给dir函数时调用,列出属性.例如,dir(obj)触发Class.__dir__(obj)方法

#  3. __getattr__(self,name)

#  仅当获取指定的属性失败,搜索过obj,Class和超类之后调用.表达式obj.no_such_attr,getattr(obj,"no_such_attr")和hasattr(obj,'no_such_attr')
#  可能会触发class.__getattr__(obj,'no_such_attr')方法,但是,仅当在obj,Class和超类中找不到指定额属性时才会触发

#  4.  __getattribute__(self,name)


#  尝试获取指定的属性时总会调用这个方法,不过,寻找的属性是特殊属性或特殊方法时除外.点号与getattr和hasattr内置函数会触发这个方法.
#  调用__getattribute__方法且抛出Attribute异常时,才会调用__getattr__方法.为了在获取obj实例的属性时不导致无限递归,__getattribute__
#  方法的实现要使用super().__getattribute__(obj,name)


#  5.    __setattr__(self,name,value)

#  尝试设置指定的属性时总会调用这个方法.点号和setattr内置函数会触发这个方法,例如,obj.attr=42 和 setattr(obj,'attr',42)都会触发
#  Class.__setattr__(obj,'attr',42)方法


#  特殊方法__getattribute__和__setattr__不管怎样都会调用,几乎会影响每一次属性存取,因此,比__getattr__方法(只处理不存在的属性名)更难正确使用.

#  与定义这些特殊方法相比,使用特性或描述符相对不易出错


#  __new__方法比new运算符好

#  在python中还有一处体现了统一访问原则(或它的变体):函数调用和对象实例化使用相同的句法:my_obj= foo()
#  其中,foo是类或其他可调用额对象