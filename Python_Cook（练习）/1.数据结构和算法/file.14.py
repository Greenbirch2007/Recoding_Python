# 1.14  对不原生支持比较操作的对象排序

# 1.14.1 问题

# 　我们想在同一个类的实例之间做排序，但是它们并不原生支持比较操作

# 　１．１４．２　解决方案

# 内建的sorted()函数可接受一个用来传递可调用对象（callable）的参数key，而该可调用对象会返回待排序对象中的某些值，
# sorted则利用这些值来比较对象。例如，如果应用中的一系列的User对象实例，而我们想通过user_id属性来对它们
# 排序，则可以提供一个可调用对象将User实例作为输入然后然后返回user_id ,如下：

class User:
    def __init__(self,user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)



users = [User(23),User(8),User(6)]
print(users)

sort_users = sorted(users,key=lambda u:u.user_id)
print(sort_users)

# 除了可以用lambda 表达式外，另一种方式是使用operator.attrgetter()


print(88*'^')

from operator import attrgetter
print(sorted(users,key=attrgetter('user_id')))

# 1.14.3 讨论
# 要使用lambda表达式还是attrgetter()或许只是一种个人爱好。但是通常来说，attrgetter()要快一些，而且具有允许同事提取
# 多个字段值的能力，这和针对字典的operator.itemgetter()的使用很类似。例如，如果User实例还有一个first_name 和　last_name
# 属性的话，可以执行如下操作：

# by_name = sorted(users,key=attrgetter('last_name','frist_name'))

# 同样值得一提的是，本节所用到的技术也适用于向min(),max()这样的函数

print(min(users,key=attrgetter('user_id')))
print(max(users,key=attrgetter('user_id')))