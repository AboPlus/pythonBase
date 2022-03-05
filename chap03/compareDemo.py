# Author: Abo
# Date: 2022/2/25 16:05

a, b = 10, 20
print(a > b)
print(a != b)

print('=============')

a, b = 10, 10
print(a == b)
print(a is b)
print(id(a), id(b))

print('========================')

list1 = [11, 22, 33, 44]
list2 = [11, 22, 33, 44]
print(list1 == list2)
print(list1 is list2)
print(list1 is not list2)
print(id(list1), id(list2))
