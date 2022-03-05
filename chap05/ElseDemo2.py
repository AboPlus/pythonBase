# Author: Abo
# Date: 2022/2/25 19:04

a = 0
while a < 3:
    pwd = input('请输入密码：')
    if pwd == '8888':
        print('ok')
        break
    else:
        print('error')
    a += 1
else:
    print('失败三次，账户已冻结')
