# Author: Abo
# Date: 2022/2/25 13:57

# 可以输出数字
print(520)
print(98.5)

# 可以输出字符串
print('helloworld')
print("helloworld")

# 可以输出含有运算符的表达式
print(3 + 5)
print(3 - 5)
print(3 * 5)
print(3 / 5)

# 可以将数据输出在文件中,注意点：1、指定盘符存在 2、使用file = 变量名
fp = open('C:/PythonDevelop/test/test.txt', 'a+') # a+:如果文件不存在就创建，存在就在文件内容的后面继续追加
print('helloworld', file=fp)
fp.close()

# 不进行换行输出
print('hello', 'world', 'python')
