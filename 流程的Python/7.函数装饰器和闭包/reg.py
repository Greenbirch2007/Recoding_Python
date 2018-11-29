
reg = []

def regi(func):
    print('running regi(%s)' % func)
    reg.append(func)
    return func


@regi
def f1():
    print('running f1()')

@regi
def f2():
    print('running f2()')


def f3():
    print('running f3()')

if __name__ == '__main__':
    print('running main()')
    print('regi-->',reg)
    f1()
    f2()
    f3()