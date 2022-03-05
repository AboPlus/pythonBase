# Author: Abo
# Date: 2022/2/25 18:52

# 从键盘录入密码，最多三次，如果正确结束循环

for _ in range(3):
    pwd = input('请输入密码：')
    if pwd == '8888':
        print('ok')
        break
    else:
        print('error')
