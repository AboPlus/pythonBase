# Author: Abo
# Date: 2022/3/4 13:21

def fun(arg1, arg2):
    print('arg1:', arg1)
    print('arg2:', arg2)

    arg1 = 100
    arg2.append(10)
    print('arg1:', arg1)
    print('arg2:', arg2)
    return


n1 = 11
n2 = [22, 33, 44]
print('n1', n1)
print('n2', n2)
fun(n1, n2)
print('n1', n1)
print('n2', n2)