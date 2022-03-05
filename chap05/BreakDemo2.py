# Author: Abo
# Date: 2022/2/25 18:56

# 从键盘录入密码，最多三次，如果正确结束循环

a = 0
while a < 3:
    pwd = input('请输入密码')
    if pwd == '8888':
        print('ok')
        break
    else:
        print('error')
    a += 1
