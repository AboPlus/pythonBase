# Author: Abo
# Date: 2022/3/4 16:23

class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print('汽车已启动...')


car = Car('宝马X5')
car.start()
print(car.brand)