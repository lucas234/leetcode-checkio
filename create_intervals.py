# coding=utf-8
# auther：Liul5
# date：2019/4/12 15:05
# tools：PyCharm
# Python：2.7.15
# https://py.checkio.org/en/mission/create-intervals/


def create_intervals(int_set):
    return


print create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [(1, 5), (7, 8), (12, 12)]
print create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)]

int_set = {6, 7, 8}  # {1, 2, 3, 4, 5, 7, 8, 12}
# new_set = {i + 1 for i in int_set}  # set(map(lambda x: x+1, int_set))
# # print int_set.difference(new_set)
# a = {i - 1 for i in new_set.difference(int_set)}
# # a = {8, 5, 12}
# print a
# print int_set.difference(new_set)
# print int_set.difference(new_set).intersection(a)
# print int_set.difference(new_set).union(a)
# import itertools
#
# i, j = itertools.tee(int_set, 2)
# for k in j:
#     print k
int_set = {1, 2, 3, 4, 5, 7, 8, 12}
a = sorted(list(int_set))
for i in range(2, len(a)):
    print a[0:i]
    # print a[1:i+2]


