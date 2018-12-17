#  第1章 python数据模型

# 数据模型其实是对python框架的描述,它规范了这门语言自身构建模块的接口,这些模块包括但不限于序列,迭代器,函数,类和上下文管理器


# python解释器[[碰到特殊的句法时,会使用特殊方法去激活一些基本的对象操作,这些特殊方法的名字以两个下划线开头,以两个下划线结尾(如__getitem__)
# 比如obj[key]背后的就是__getitem__方法,为了能求得my_collection[key]的值,解释器实际上会调用my_collection.__getitem__(key)

# 这些特殊方法名能让你自己的对象实现和支持以下的语言框架,并与之交互

# 1.迭代
# 2. 集合类
# 3.属性访问
# 4. 运算符重载
# 5. 函数和方法的调用
# 6.对象的创建和销毁
# 7.字符串表示的形式和格式
# 8.管理上下文(即with块)

#  magic和dunder

#  魔术方法(magic method)是特殊方法的昵称.特殊方法都是叫双下方法(dunder method)


#  1.1 一摞python风格的指派

#  示例1-1 一摞有序的纸牌,展示如何实现__getitem__和__len__这两个特殊方法

import collections

Card = collections.namedtuple('Card',['rank','suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):  # 实例化类
        self._cards = [Card(rank,suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)


    def __getitem__(self, position):
        return self._cards[position]


# 首先,我们用collections.namedtuple构建一个简单的类来表示一张纸牌.namedtuple,具名元组,用以构建只有少数属性单是没有方法的对象,比如数据库条目
#  利用namedtuple,可以轻松得到一个纸牌对象


b_card  = Card('8','diamond')
print(b_card)


#  再来关注FrenhDeck这个类,它短小精悍.首先,它跟任何标准Python集合类型一样,可以用len()函数来查看有多少张牌

deck = FrenchDeck()
print(len(deck))


#  也可以切片,比如deck[0],deck[-1]分别表示第一张和最后一张.这都是由__getitem__方法提供的

print(deck[0])
print(deck[-1])

# python内置了从一个序列中随机选出一个元素的函数random.choice,

from random import choice

print(88*'~')
print(choice(deck))
print(choice(deck))
print(choice(deck))

#  这里可以看到通过实现特殊方法来利用Python数据模型的两个好处

#  1. 作为你类的用户,不必去记住标准操作的各种名称
#  2. 可以更加方便的利用python标准库,如random.choice,不用重复造轮子


#  因为__getitem__方法把[]操作交给了self._cards李彪,所以我们的deck类自动支持切片(slicing)操作

# print(deck[:3])
# print(88*'~')
# print(deck[12::13])  # 从第12张开始每隔13张,拿一张

#  另外,仅仅实现__getitem__方法,就可以迭代

for card in deck:
    print(card)

# 也可以进行反向迭代

for card in reversed(deck): # 反向迭代
    print(card)

# doctest中的省略

#  迭代通常是隐式的，比如说一个集合类型没有实现__contains__方法，那么in运算符就会按顺序做一次迭代搜索．于是，in运算符可以用在我们的FrenchDeck类上，因为它是可迭代的

#  那么排序呢？按照常规，用点数来判定扑克牌的大小


