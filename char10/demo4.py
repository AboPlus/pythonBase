# Author: Abo
# Date: 2022/3/4 11:56

s = 'hello,Python'
# 居中对齐
print(s.center(20, '*'))

# 左对齐
print(s.ljust(20, '*'))
print(s.ljust(20))

# 右对齐
print(s.rjust(20, '*'))
print(s.rjust(20))

# 右对齐 使用0进行填充
print(s.zfill(20))
print('-8910'.zfill(18))
