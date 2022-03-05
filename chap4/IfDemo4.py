# Author: Abo
# Date: 2022/2/25 18:07

isVip = input('你是会员吗？y/n')

if isVip=='y':
    money = int(input('请输入消费的金额：'))
    if money >= 200:
        if money >= 400:
            print('八折')
        else:
            print('九折')
    else:
        print('不打折')
else:
    print('不是会员，不打折')



