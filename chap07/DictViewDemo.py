# Author: Abo
# Date: 2022/3/3 20:53

scores = {'key1': 'value1', 'key2': 'value2', 'key3': 3}

# 获取所有的key
keys = scores.keys()
print(keys, type(keys))
print(list(keys))  # 将所有的key组成的视图转换成列表

# 获取所有的value
values = scores.values()
print(values, type(values))
print(list(values))

# 获取所有的key-value
items = scores.items()
print(items, type(items))
print(list(items))  # 转换之后的列表元素是由元组组成
