# Author: Abo
# Date: 2022/3/3 22:15

# 集合的数学操作
s1 = {10, 20, 30, 40}
s2 = {20, 30, 40, 50, 60}

# 交集  intersection() 等价于 &
print(s1.intersection(s2))
print(s1 & s2)

# 并集  union() 等价于 |
print(s1.union(s2))
print(s1 | s2)

# 差集  difference()  等价于 -
print(s1.difference(s2))  # s1 - s2
print(s1 - s2)
print(s2.difference(s1))  # s2 - s1
print(s2 - s1)

# 对称差集
print(s1.symmetric_difference(s2))

