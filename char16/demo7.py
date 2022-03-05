# Author: Abo
# Date: 2022/3/5 12:31

file = open('a.txt', 'r', encoding='UTF-8')
file.seek(2)
print(file.read())
file.close()
