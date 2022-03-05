# Author: Abo
# Date: 2022/2/25 18:01

grade = int(input('请输入你的分数：'))

if grade > 100 or grade < 0:
    print('不合法')
elif 90 <= grade < 100:
    print("优秀")
elif 80 <= grade < 90:
    print('良好')
elif 60 <= grade < 80:
    print('合格')
else:
    print('不合格')
