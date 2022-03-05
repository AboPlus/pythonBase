# Author: Abo
# Date: 2022/3/3 22:07

s1 = {10, 20, 30, 40}
s2 = {20, 30, 10, 40}

print(s1 == s2)
print(s1 != s2)

'''
    一个集合是否是另一个集合的子集
'''
s1 = {10, 20, 30, 40, 50, 60}
s2 = {10, 20, 30, 40}
s3 = {10, 20, 90}

print(s2.issubset(s1))
print(s3.issubset(s1))

'''
    一个集合是否是另一个集合的超集
'''
print(s1.issuperset(s2))
print(s1.issuperset(s3))

'''
    两个集合是否没有交集
'''
print(s2.isdisjoint(s3))
s4 = {100, 200, 300}
print(s2.isdisjoint(s4))
