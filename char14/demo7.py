# Author: Abo
# Date: 2022/3/4 17:38

class Animal:
    def eat(self):
        print('动物要吃东西')


class Dog(Animal):
    def eat(self):
        print('狗吃肉')


class Cat(Animal):
    def eat(self):
        print('猫吃鱼')


class Person:
    def eat(self):
        print('人吃五谷杂粮')


# 定义一个函数
def fun(obj):
    obj.eat()


fun(Cat())
fun(Dog())
fun(Animal())
print('------------------')
fun(Person())
