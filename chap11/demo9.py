# Author: Abo
# Date: 2022/3/4 14:01

def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n - 1)


print(fac(6))
