# Author: Abo
# Date: 2022/3/3 21:13

# 可变序列  列表 字典
lst = [10, 20, 45]
print(id(lst))
lst.append(300)
print(id(lst))

print('-------------------------------------')

# 不可变序列  字符串，元组
s = 'hello'
print(id(s))
s = s + 'world'
print(id(s))
