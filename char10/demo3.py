# Author: Abo
# Date: 2022/3/4 11:50

# 字符串中的大小写转换的方法
s = 'hello,python'

s1 = s.upper()  # 转换成大写之后会产生一个新的字符串对象
print(s, id(s))
print(s1, id(s1))

print('-------------------------------')

s2 = s1.lower()
print(s, id(s))
print(s1, id(s1))
print(s2, id(s2))

print('-------------------------------')

s3 = 'HelLo, PyTHoN'
s4 = s3.swapcase()
print(s4)

print('------------------------------')
s5 = 'hello, Python'
print(s5.capitalize())
print(s5.title())
