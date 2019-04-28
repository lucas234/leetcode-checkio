# coding=utf-8
# auther：Liul5
# date：2019/4/28 9:15
# tools：PyCharm
# Python：2.7.15
# https://py.checkio.org/en/mission/wild-dogs/
from itertools import combinations
from math import sqrt


def get_line(p1, p2):
    """已知直线上两点求直线的一般式方程
    已知直线上的两点P1(X1,Y1) P2(X2,Y2)， P1 P2两点不重合。
    则直线的一般式方程AX+BY+C=0中，A B C分别等于：
    A = Y2 - Y1
    B = X1 - X2
    C = X2*Y1 - X1*Y2"""
    a = p2[1] - p1[1]
    b = p1[0] - p2[0]
    c = p2[0] * p1[1] - p1[0] * p2[1]
    return a, b, c


def is_on_the_line(point, line):
    """
    whether the point is on the line
    :param point:
    :param line:
    :return:
    """
    result = point[0] * line[0] + point[1] * line[1] + line[2]
    if result:
        return False
    else:
        return True


def get_distance(line, point=(0, 0)):
    """
    get the distance from point to line
    point:(x, y) line(a,b,c)
    distance = abs(a*x+b*x+c)/sqrt(a**2+b**2)
    :param point:
    :param line:
    :return:
    """
    a, b, c = line[0], line[1], line[2]
    x, y = point[0], point[1]
    return abs(a * x + b * x + c) / sqrt(a ** 2 + b ** 2)


def wild_dogs(points):
    all_lines = [get_line(*i) for i in combinations(points, 2)]
    line_points = []
    for i in set(all_lines):
        count = 0
        for j in points:
            if is_on_the_line(j, i):
                count += 1
        line_points.append((i, count))
    _count = max(line_points, key=lambda x: x[1])[1]
    _line = filter(lambda x: x[1] == _count, line_points)
    distance = round(min([get_distance(i[0]) for i in _line]), 2)
    return distance


print wild_dogs([(7, 122), (8, 139), (9, 156), (10, 173), (11, 190), (-100, 1)]) == 0.18
