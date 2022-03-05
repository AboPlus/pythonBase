# Author: Abo
# Date: 2022/2/25 18:42

"""
    输出100 - 999 之间的水仙花数
    举例：
    153=3*3*3+5*5*5=1*1*1
"""

for item in range(100, 1000):
    ge = item % 10
    shi = item // 10 % 10
    bai = item // 100
    if ge ** 3 + shi ** 3 + bai ** 3 == item:
        print(item)
