# Author: Abo
# Date: 2022/3/4 18:10

class CPU:
    pass


class Disk:
    pass


class Computer:
    def __init__(self, cpu, disk):
        self.cpu = cpu
        self.disk = disk


# 变量的赋值
cpu1 = CPU()
cpu2 = cpu1
print(id(cpu1), id(cpu2))

print('---------------------------')

# 类的浅拷贝
disk = Disk()
computer = Computer(cpu1, disk)

# 浅拷贝
import copy

computer2 = copy.copy(computer)

print(computer, computer.cpu, computer.disk)
print(computer2, computer2.cpu, computer2.disk)

print('---------------------------------------')
computer3 = copy.deepcopy(computer)
print(computer, computer.cpu, computer.disk)
print(computer3, computer3.cpu, computer3.disk)
