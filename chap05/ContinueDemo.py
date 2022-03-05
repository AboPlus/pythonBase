# Author: Abo
# Date: 2022/2/25 18:59

# 输出1-50之间所有5的倍数

for item in range(1, 51):
    if item % 5 != 0:
        continue
    else:
        print(item)
