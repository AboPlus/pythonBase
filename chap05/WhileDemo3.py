# Author: Abo
# Date: 2022/2/25 18:33

# 计算1-100之间的偶数和

a = 1
res = 0
while a <= 100:
    if a % 2 == 0:
        res += a
    a += 1
print(res)
