# Author: Abo
# Date: 2022/3/5 12:27

src_file = open('logo.jpg', 'rb')
target_file = open('copylogo.jpg', 'wb')
target_file.write(src_file.read())
target_file.close()
src_file.close()
