# Author: Abo
# Date: 2022/3/4 12:06

s = 'hello,python'

# 判断是否是合法的标识符
print('1.', s.isidentifier())
print('2.', 'hello'.isidentifier())
print('3.', 'hello_python'.isidentifier())
print('4.', 'hello_python_1234'.isidentifier())
print('5.', '张三_hello_12345'.isidentifier())

print('------------------------')

# 判断字符串是否由空格、制表符组成
print('6.', '\t'.isspace())
print('7.', ''.isspace())
print('8.', ' '.isspace())

print('------------------------')

# 判断是否由字母组成（包含中文字符）
print('9.', 'abc'.isalpha())
print('10.', '张三'.isalpha())
print('11.', '张三1'.isalpha())

print('------------------------')

# 判断是否由十进制数字组成（阿拉伯数字）
print('12', '123'.isdecimal())
print('13', '123四'.isdecimal())

print('------------------------')

# 判断是否由数字组成(阿拉伯数字、中文数字、罗马数字....)
print('14', '123'.isnumeric())
print('15', '123四'.isnumeric())

print('------------------------')

# 判断是否由数字和字母组成
print('16', 'abc1'.isalnum())
print('17', '张三ab123'.isalnum())
print('18', '张三ab!123'.isalnum())
