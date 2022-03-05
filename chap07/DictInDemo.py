# Author: Abo
# Date: 2022/3/3 20:48

scores = {'key1': 'value1', 'key2': 'value2', 'key3': 3}

print('key1' in scores)
print('key1' not in scores)

del scores['key1']  # 删除指定的k-v
print(scores)

scores['key4'] = 'value4'  # 新增
print(scores)

scores['key4'] = 'value4444'  # 修改
print(scores)

scores.clear()  # 清空字典k-v
print(scores)
