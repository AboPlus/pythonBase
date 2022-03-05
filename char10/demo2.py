# Author: Abo
# Date: 2022/3/4 11:45

s = 'hello world'
print(s.index('o'))
print(s.rindex('o'))

s1 = 'hello hello'
print(s1.find('lo'))
print(s1.rfind('lo'))

# print(s.index('k'))  # 异常
print(s.find('k'))  # 未异常  输出 -1
