# Author: Abo
# Date: 2022/3/4 15:17

try:
    a = int(input('请输入一个整数：'))
    b = int(input('请输入另一个整数：'))
except BaseException as e:
    print('出错了')
    print(e)
else:
    print(a / b)
