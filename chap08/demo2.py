# Author: Abo
# Date: 2022/3/3 21:16

'''
    元组的创建方式
        1. 使用()
        2. 使用内置函数tuple
'''

t = ('Python', 'world', 98)
print(t)
print(type(t))

t1 = tuple(('Python', 'world', 98))
print(t1)
print(type(t1))

t2 = 'Python', 'world', 88
print(t2)
print(type(t2))

t3 = ('Python')
print(type(t3))  # str
t4 = ('Python',)  # 只包含一个元素的元组 不能省略逗号
print(type(t4))

t5 = 'Python',  # 只包含一个元素的元组 不能省略逗号
print(type(t5))

t6 = ()
t7 = tuple()

l1 = []
l2 = list()

d1 = {}
d2 = dict()
