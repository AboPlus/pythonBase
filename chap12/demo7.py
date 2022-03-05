# Author: Abo
# Date: 2022/3/4 15:25

# print(10 / 0)
import traceback

try:
    print('----------------')
    print(1 / 0)
except:
    traceback.print_exc()
