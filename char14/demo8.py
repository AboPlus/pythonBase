# Author: Abo
# Date: 2022/3/4 17:44

# print(dir(object))

class A:
    pass


class B:
    pass


class C(A, B):
    def __init__(self, name, age):
        self.name = name
        self.age = age


x = C('Jack', 20)
print(x.__dict__)
print(C.__dict__)

print('-------------------------')

print(x.__class__)
print(C.__bases__)
print(C.__base__)
print(C.__mro__)

print(A.__subclasses__())
