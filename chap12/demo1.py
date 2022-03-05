# Author: Abo
# Date: 2022/3/4 14:33

lst = [{'rating': [9.7, 2062397], 'id': '1292052', 'type': ['犯罪', '剧情'], 'title': '肖申克的救赎', 'actors': ['蒂姆', '摩根']}]

name = input('请输入你要查询的演员：')
for item in lst:
    act_lst = item['actors']
    if name in act_lst:
        print(name + '出演了：' + item['title'])
