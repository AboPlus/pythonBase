# Author: Abo
# Date: 2022/2/25 15:56

print(1 + 1)
print(1 - 1)
print(5 * 3)
print(3 / 5)
print(6 // 5)
print(7 % 5)
print(2 ** 8)
print(-6 // 5)

print('======================')

a = 3 + 4
a *= 2
print(a)

b = c = a
print(a, b, c)
print(id(a), id(b), id(c))

a, b, c = 10, 20, 30
print(a, b, c)
print(id(a), id(b), id(c))

print('交换之前:', a, b)
a, b = b, a
print('交换之后:', a, b)
