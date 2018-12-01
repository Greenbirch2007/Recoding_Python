
from clockdeco import clock



@clock
def fiboacci(n):
    if n <2:
        return n
    return fiboacci(n-2)  + fiboacci(n-1)


if __name__ == '__main__':
    print(fiboacci(6))