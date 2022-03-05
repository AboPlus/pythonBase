# Author: Abo
# Date: 2022/2/25 18:14

num_a = int(input('请输入一个整数：'))
num_b = int(input('请输入另一个整数：'))

# if num_a > num_b:
#     print(num_a)
# elif num_a == num_b:
#     print(num_a)
# else:
#     print(num_b)

print('使用条件表达式进行比较')
print(num_a if num_a >= num_b else num_b)
