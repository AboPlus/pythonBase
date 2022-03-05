# Author: Abo
# Date: 2022/2/25 17:54

balance = 1000

amount = int(input('请输入取款金额：'))
if balance >= amount:
    balance = balance - amount
    print('取款成功，余额为：' + str(balance))
else:
    print('余额不足！')
