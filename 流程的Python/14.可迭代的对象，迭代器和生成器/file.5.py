#  14.10   python3.3  中新出现的句法:yield from


# 如果生成器函数需要产出另一个生成器的值,传统的解决方法是使用嵌套的for循环.
# 下面就实现一个chain生成器

def chain(*iterables):
    for it in iterables:
        for i in it:
            yield i


s = 'ABC'
t = tuple(range(3))
print(t)
print(list(chain(s,t)))