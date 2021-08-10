# coding=utf-8
# auther：Liul5
# date：2019/5/8 14:29
# tools：PyCharm
# Python：2.7.15
# https://py.checkio.org/en/mission/merge-intervals/


def merge_intervals(args):
    response, b, e = [], 0, 0
    if not args:
        return response
    int_set = []
    for i in args:
        x, y = i
        int_set = int_set + list(range(x, y+1))
    int_set = set(int_set)
    int_set = sorted(list(int_set))
    for i in range(1, len(int_set)):
        if int_set[i] - int_set[e] > 1:
            response.append((int_set[b], int_set[e]))
            b = i
        e = i
    if (int_set[b], int_set[e]) not in response:
        response.append((int_set[b], int_set[e]))
    return response


print merge_intervals([(1, 4), (2, 6), (8, 10), (12, 19)]) == [(1, 6), (8, 10), (12, 19)]
print merge_intervals([(1, 12), (2, 3), (4, 7)]) == [(1, 12)]
print merge_intervals([(1, 5), (6, 10), (10, 15), (17, 20)]) == [(1, 15), (17, 20)]


#
# def merge_intervals(intervals):
#     if not intervals:
#         return []
#     imin, imax = intervals[0][0], intervals[0][1]
#     out = []
#     for i in intervals:
#         if set(range(*i)) & set(range(imin, imax)) or i[0] - imax <= 1:
#             imin, imax = min([imin, i[0]]), max([imax, i[1]])
#         else:
#             out.append(tuple([imin, imax]))
#             imin, imax = i[0], i[1]
#     else:
#         out.append(tuple([imin, imax]))
#     return out

#
# def merge_intervals(intervals):
#     if len(intervals) < 2:
#         return intervals
#     new = [intervals[0]]
#     for a, b in intervals[1:]:
#         if a > new[-1][1] + 1:
#             new.append((a, b))
#         elif new[-1][1] < b:
#             new[-1] = new[-1][0], b
#     return new
# print merge_intervals([(1, 4), (2, 6), (8, 10), (12, 19)])