# Author: Abo
# Date: 2022/3/3 21:27

t = (10, [20, 30], 9)
print(t)
print(type(t))

print(t[0], type(t[0]))
print(t[1], type(t[1]))
print(t[2], type(t[2]))

# t[1] = 100  # TypeError: 'tuple' object does not support item assignment   元组不允许修改元素

t[1].append(100)
print(t)
