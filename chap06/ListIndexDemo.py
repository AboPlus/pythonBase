# Author: Abo
# Date: 2022/3/3 13:12

lst = ['hello', 'world', 98, 'hello']

print(lst.index('hello'))  # 如果列表中有相同元素只返回列表中第一次出现该元素的索引
# print(lst.index('python')) # 查找列表中不存在的元素会报错：ValueError: 'python' is not in list

print(lst.index('hello', 1, len(lst)))

print(len(lst))
