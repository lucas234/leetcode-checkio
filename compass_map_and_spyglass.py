# coding=utf-8
# auther：Liul5
# date：2019/4/8 11:06
# tools：PyCharm
# Python：2.7.15
# https://py.checkio.org/en/mission/compass-map-and-spyglass/


def navigation(_list):
    location = {j: (index1, index2) for index1, i in enumerate(_list) for index2, j in enumerate(i) if
                j in ['Y', 'C', 'M', 'S']}
    path = map(lambda x: max([abs(x[0] - location.get("Y")[0]), abs(x[1] - location.get("Y")[1])]), location.values())
    return sum(path)


print navigation([['Y', 0, 0, 0, 'C'],
                  [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  ['M', 0, 0, 0, 'S']]) == 11  # 4 steps from Y to C, 4 from Y to S and 3 from Y to M
