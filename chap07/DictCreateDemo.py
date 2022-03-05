# Author: Abo
# Date: 2022/3/3 21:07

items = ['Fruits', 'Books', 'Others']
prices = [96, 78, 55]

d = {item.upper(): price for item, price in zip(items, prices)}
print(d)
