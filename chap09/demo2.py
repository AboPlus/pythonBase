# Author: Abo
# Date: 2022/3/3 22:00

s = {10, 20, 30, 40, 50, 60}
print(10 in s)
print(10 not in s)

# 集合元素的新增操作： add：一次添加一个元素  update：一次至少添加一个元素
s.add(60)
print(s)
s.add(70)
print(s)
s.update({200, 400, 300})
print(s)
s.update([11, 111, 111])
print(s)
s.update((2, 22, 222))
print(s)

s.remove(2)
print(s)
# s.remove(999) # 如果移除的元素不存在 会报异常  KeyError: 999
s.discard(999)  # 如果移除的元素不存在 不会报异常
print(s)
s.pop()  # 随机删除一个元素  不知道删除的是谁  不能给参数
print(s)

s.clear()  # 清空集合中的元素
print(s)
