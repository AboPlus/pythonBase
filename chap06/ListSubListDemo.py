# Author: Abo
# Date: 2022/3/3 13:19

lst = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# print(lst[1:6])
# print(lst[1:6:1])

print('原列表', id(lst))
lst2 = lst[1:6]  # 默认步长为一
print('切片后列表', id(lst2))

print(lst[1:6:2])

print(lst[:6:2])

print(lst[4::1])

print('=======================step步长为负数的情况=======================')

print(lst[::-1])

print(lst[7::-1])
print(lst[7:0:-1])
print(lst[7::-2])
