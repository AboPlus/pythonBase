# Author: Abo
# Date: 2022/3/3 13:30

lst = [10, 20, 30]
lst.append(100)
print(lst, id(lst))

# lst.append(lst)  # 将列表当做一个元素添加到列表中  (列表中存储列表)
# print(lst)

lst.extend(lst)
print(lst, id(lst))

lst.insert(1, 90)
print(lst)

lst3 = [True, False, 'hello']
lst[1:] = lst3
print(lst)

