# Author: Abo
# Date: 2022/3/3 20:43

scores = {'key1': 'value1', 'key2': 'value2', 'key3': 3}
print(scores['key1'])

s = scores.get('key2')
print(s)

i = scores.get('key3')
print(i)

# print(scores['key4']) # 报错
print(scores.get('key4'))  # None

print(scores.get('key3', 1))  # 输出3  因为字典中存在key
print(scores.get('key4', 1))  # 输出1 因为字典中不存在key4 所以是None  是None时会输出默认值1
