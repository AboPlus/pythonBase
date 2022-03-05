# Author: Abo
# Date: 2022/3/4 16:26

class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def show(self):
        print(self.name, self.__age)


stu = Student('张三', 20)
print(stu.name)
# print(stu.__age)
print(dir(stu))
# print(stu._Student__age)





