# Author: Abo
# Date: 2022/2/25 14:38

name = '玛丽亚'
print(name)
name = '楚留香'
print(name)
print('标识', id(name))
print('类型', type(name))
print('值', name)

print('============整数=============')

num = -98
print(num)
print('类型', type(num))
print('十进制', 175)
print('二进制', 0b10101111)
print('八进制', 0o257)
print('十六进制', 0xABC25)

print('============浮点数=============')

pi = -3.1415926
print(pi)
print('类型', type(pi))

n1 = 1.1
n2 = 2.2
print(n1 + n2)

from decimal import Decimal

print(Decimal('1.1') + Decimal('2.2'))

print('============布尔型=============')

f1 = True
f2 = False
print(f1)
print(f2)
print('类型', type(f1))
print('类型', type(f2))

print(f1 + 1)
print(f2 + 1)

print('============字符串=============')
str1 = '人生苦短，我用python'
str2 = "人生苦短，我用python"
str3 = '''人生苦短，
我用python'''
str4 = """人生苦短
，我用python"""
print(str1, type(str1))
print(str2, type(str2))
print(str3, type(str3))
print(str4, type(str4))
