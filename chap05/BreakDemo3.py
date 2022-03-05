# Author: Abo
# Date: 2022/3/3 12:53

for i in range(5):
    for j in range(1, 11):
        if j % 2 == 0:
            # break
            continue
        # print(i, j)
        print(j, end='\t')
    print('')
