# Author: Abo
# Date: 2022/2/25 14:10

# 转义字符
print('hello\nworld') # \n:换行 newLine
print('hello\tworld') # \t:缩进 tab
print('helloo\tworld')
print('hellooo\tworld')
print('helloooo\tworld')
print('hello\rworld') # \r:回车 return
print('hello\bworld') # \b:退格

print('http:\\www.baidu.com')
print('http:\\\\www.baidu.com')

print('老师说:\'大家好\'')

# 原字符,不希望字符串中的转义字符起作用，就用原字符，就是在祖父穿之前加上r或者R
print(r'hello\nworld')
print(r'hello\nworld')