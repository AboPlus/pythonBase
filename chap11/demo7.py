# Author: Abo
# Date: 2022/3/4 13:49

def fun(a, b=10):
    print('a=', a)
    print('b=', b)


def fun2(*args):
    print(args)


def fun3(**args):
    print(args)


def fun4(a, b, c, d):
    print('a=', a)
    print('b=', b)
    print('c=', c)
    print('d=', d)


def fun5(a, b, *c, d, **args):
    pass


def fun6(*args1, **args2):
    pass


def fun7(a, b, *args1, **args2):
    pass


fun(1)
fun2(10, 20, 30)
fun3(a=10, b=20, c=30)
fun4(10, 20, 30, 40)
fun4(d=10, b=20, a=30, c=40)
fun4(10, 20, d=30, c=40)
