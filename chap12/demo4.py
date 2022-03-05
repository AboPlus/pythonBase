# Author: Abo
# Date: 2022/3/4 15:16

try:
    a = int(input('请输入一个整数：'))
    b = int(input('请输入另一个整数：'))
    print(a / b)
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
print('程序结束')
