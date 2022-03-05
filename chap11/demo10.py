# Author: Abo
# Date: 2022/3/4 14:03

def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(6))

print('------------------------------------')

for i in range(1, 7):
    print(fib(i))
