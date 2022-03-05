# Author: Abo
# Date: 2022/3/4 13:40

def fun(*args):
    print(args)


fun(10)
fun(10, 20, 30, 40, 50)


def fun2(**args):
    print(args)


fun2(a=1)
fun2(a=1, b=2, c=3, d=4)


def fun3(args1, *args2):
    print(args1)
    print(args2)


fun3(1, 2, 3, 4, 5, 6)
