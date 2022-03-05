# Author: Abo
# Date: 2022/3/3 20:59

scores = {'key1': 'value1', 'key2': 'value2', 'key3': 3}

for item in scores:
    print(item, scores[item], scores.get(item))
