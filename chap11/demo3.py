# Author: Abo
# Date: 2022/3/4 13:26

def fun(num):
    odd = []  # 存奇数
    even = []  # 存偶数
    for i in num:
        if i % 2:
            odd.append(i)
        else:
            even.append(i)
    return odd, even


t = fun([10, 29, 34, 23, 44, 53, 55])
print(t)
t_odd = t[0]
t_even = t[1]
print(t_odd)
print(t_even)
