# Author: Abo
# Date: 2022/3/4 15:41

class Student:  # Student为类的名称(类名)由一个或多个单词组成，每个单词的首字母大写，其余小写
    native_pace = '吉林'  # 直接写在类里的变量，称为类属性

    def __init__(self, name, age):
        self.name = name  # self.name 称为实例属性，进行了一个赋值的操作，将局部变量的name的值赋给实体属性
        self.age = age

    # 实例方法
    def eat(self):
        print('学生在吃饭...')

    # 静态方法
    @staticmethod
    def method():
        print('我使用了@staticmethod进行修饰，所以我是静态方法')

    # 类方法
    @classmethod
    def cm(cls):
        print('我是类方法，因为我使用了classmethod进行修饰')


stu1 = Student('张三', 20)
print(id(stu1))
print(type(stu1))
print(stu1)
print(stu1.name)
print(stu1.age)
stu1.eat()
stu1.cm()
stu1.method()

Student.eat(stu1)
