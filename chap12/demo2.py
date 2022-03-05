# Author: Abo
# Date: 2022/3/4 15:11

try:
    a = int(input('请输入一个整数：'))
    b = int(input('请输入另一个整数：'))
    print(a / b)
except ZeroDivisionError:
    print('分母不可为零')
print('程序结束')
