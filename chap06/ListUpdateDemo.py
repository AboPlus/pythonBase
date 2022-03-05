# Author: Abo
# Date: 2022/3/3 18:20

lst = [10, 20, 30, 40]
# 一次修改一个值
print(lst, id(lst))

lst[2] = 100
print(lst, id(lst))

lst[1:3] = [300, 400, 500]
print(lst, id(lst))
