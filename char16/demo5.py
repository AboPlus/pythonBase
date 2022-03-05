# Author: Abo
# Date: 2022/3/5 12:31

file = open('a.txt', 'r', encoding='UTF-8')
# print(file.read(2))
# print(file.readline())
print(file.readlines())
file.close()