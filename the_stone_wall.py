# coding=utf-8
# auther：Liul5
# date：2019/4/8 13:08
# tools：PyCharm
# Python：2.7.15
# https://py.checkio.org/en/mission/the-stone-wall/
from collections import Counter


def stone_wall(stone_str):
    if "0" not in stone_str:
        return 0
    stone_str = stone_str.split()
    index = [index1 for index, i in enumerate(stone_str) for index1, j in enumerate(i) if j == "0"]
    return sorted(Counter(index).items(), key=lambda x: (x[1], -x[0]), reverse=True)[0][0]


print stone_wall('''
##########
####0##0##
00##0###00
''') == 4


# cols = lambda multiline: zip(*multiline.strip().split('\n'))
# stone_wall = lambda wall: min(enumerate(cols(wall)), key=lambda x: x[1].count('#'))[0]
