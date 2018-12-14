
registry = set()

def register(activate=True):
    def decorate(func):
        print('running regsiter(activate=%s)->decorate(%s)'%(activate,func))
        if activate:
            registry.add(func)

        else:
            registry.discard(func)

        return func
    return decorate


@register(activate=False)
def f1():
    print('running f1()')

@register
def f2():
    print('running f2()')

def f3():
    print('running f3()')