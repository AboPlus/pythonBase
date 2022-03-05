# Author: Abo
# Date: 2022/3/4 12:22

print('apple' > 'app')  # T
print('apple' > 'banana')  # F

print(ord('a'))
print(ord('b'))

print(chr(97), chr(98))

'''
    == 与 is 的区别
    == 比较的是 value
    is 比较的是内存地址是否相同(id)
'''
a = b = 'python'
c = 'python'
print(a == b)
print(b == c)

print(a is b)
print(a is c)
print(b is c)
