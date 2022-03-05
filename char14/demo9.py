# Author: Abo
# Date: 2022/3/4 17:49

a = 20
b = 100
c = a + b
d = a.__add__(b)

print(c)
print(d)


class Student:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        return self.name + other.name


stu1 = Student('张三')
stu2 = Student('李四')

s = stu1 + stu2
print(s)
