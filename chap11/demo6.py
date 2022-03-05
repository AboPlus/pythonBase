# Author: Abo
# Date: 2022/3/4 13:46

def fun(a, b, c):
    print('a=', a)
    print('b=', b)
    print('c=', c)


lst = [10, 20, 30]
fun(*lst)

d = {'a': 100, 'b': 200, 'c': 300}
fun(**d)
