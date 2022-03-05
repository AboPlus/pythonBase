# Author: Abo
# Date: 2022/3/3 18:12

lst = [10, 20, 30, 40, 50, 60, 70, 80, 30]
lst.remove(30)  # remove: 从列表中移除一个元素，如果有重复元素则只移除第一次出现该元素的位置
print(lst)

lst.pop()
print(lst)

lst.pop(1)  # pop：如果不指定索引，则删除的是列表中的最后一个元素
print(lst)

lst.pop(0)
print(lst)

print('--------------------切片,删除至少一个元素，将产生一个新的列表对象---------------------')

new_lst = lst[1:3]
print('原列表', lst)
print('切片后列表', new_lst)

'''
    不产生新的列表对象，二十删除原列表中的内容
'''
lst[1:3] = []
print(lst)

lst.clear()  # 清除列表元素
print(lst)

# del lst  # 删除列表
# print(lst)



