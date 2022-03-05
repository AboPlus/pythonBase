# Author: Abo
# Date: 2022/3/5 12:33

file = open('a.txt', 'a', encoding='UTF-8')
# file.write('hello')
lst = ['java', 'go', 'python']
file.writelines(lst)
file.close()