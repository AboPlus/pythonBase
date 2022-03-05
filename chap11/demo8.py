# Author: Abo
# Date: 2022/3/4 13:56

def fun(a, b):
    c = a + b
    return c


name = 'Abo'
print(name)


def fun2():
    print(name)


fun2()


def fun3():
    global age
    age = 20
    print(age)


fun3()
print(age)