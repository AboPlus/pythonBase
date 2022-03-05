# Author: Abo
# Date: 2022/2/25 18:37

for item in 'Python':
    print(item)

for item in range(10):
    print(item)

for _ in range(5):
    print('人生苦短，我用Python')

res = 0
for item in range(1, 101):
    if not bool(item % 2):
        res += item
print('1-100偶数和为：', res)
