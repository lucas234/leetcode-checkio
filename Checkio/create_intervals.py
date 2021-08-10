# coding=utf-8
# auther：Liul5
# date：2019/4/12 15:05
# tools：PyCharm
# Python：2.7.15
# https://py.checkio.org/en/mission/create-intervals/


def create_intervals(int_set):
    response, b, e = [], 0, 0
    if not int_set:
        return response
    int_set = sorted(list(int_set))
    for i in range(1, len(int_set)):
        if int_set[i] - int_set[e] > 1:
            response.append((int_set[b], int_set[e]))
            b = i
        e = i
    if (int_set[b], int_set[e]) not in response:
        response.append((int_set[b], int_set[e]))
    return response


print create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [(1, 5), (7, 8), (12, 12)]
print create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)]


# from itertools import groupby
#
# def create_intervals(data):
#     return [(r[0], r[-1]) for r in (list(zip(*g))[1] for _, g in groupby(enumerate(sorted(data)), lambda i: i[1] - i[0]))]

# def create_intervals(s):
#     if len(s) == 0:
#         return []
#     s = sorted(s)
#     ss = s[1:] + [s[0]]
#     idx = [n for n in range(0, len(s) - 1) if (ss[n] - s[n]) != 1]
#     idx = sorted(idx + [x + 1 for x in idx])
#     idx = [0] + idx + [len(s) - 1]
#
#     return [(s[idx[n]], s[idx[n + 1]]) for n in range(0, len(idx), 2)]