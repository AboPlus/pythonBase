# Author: Abo
# Date: 2022/2/25 19:02

for item in range(3):
    pwd = input('请输入密码:')
    if pwd == '8888':
        print('ok')
        break
    else:
        print('error')
else:
    print('失败三次，账户已锁定')
