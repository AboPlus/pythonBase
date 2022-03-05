# Author: Abo
# Date: 2022/3/3 18:26

lst = [20, 40, 10, 98, 54]
print('排序前的列表', lst, id(lst))

# 开始排序 调用列表对象的sort方法，默认升序排序,默认reverse=False
lst.sort()
print('排序后的列表', lst, id(lst))

# 通过指定关键字参数，将列表中的元素进行降序排序
lst.sort(reverse=True)
print('排序后的列表', lst, id(lst))

lst.sort(reverse=False)
print('排序后的列表', lst, id(lst))

new_list = sorted(lst)
print(new_list, id(new_list))

desc_list = sorted(lst, reverse=True)
print(desc_list, id(desc_list))
