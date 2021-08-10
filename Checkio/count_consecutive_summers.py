# coding=utf-8
# auther：Liul5
# date：2019/4/8 14:33
# tools：PyCharm
# Python：2.7.15
# https://py.checkio.org/en/mission/count-consecutive-summers/
# from __future__ import division


def median(medians, length):
    if length % 2 == 0:
        num = length / 2
        if medians - num > 0:
            result = range(medians - num, medians + num), range(medians - num + 1, medians + num + 1)
            # print result
            return map(sum, result)
    else:
        num = (length - 1) / 2
        if medians - num >= 0:
            result = range(medians - num, medians + num + 1)
            return [sum(result)]


def count_consecutive_summers(num):
    i = 1
    count = 0
    while (num / i) >= 1:
        temp = median(num / i, i)
        if temp and num in temp:
            count += 1
            # print i, num / i, num, temp
        i += 1
    return count


print count_consecutive_summers(42) == 4
print count_consecutive_summers(99) == 6


print count_consecutive_summers(105)




# from math import ceil, sqrt
# count_consecutive_summers = lambda a: sum(not (a-(i-1)*i/2)%i for i in range(1, ceil((1+sqrt(1+8*a))/2)))


# def count_consecutive_summers(a):
#     _sum, i = 0, 1
#     while a / i >= i / 2:
#         _sum += (a / i - (i % 2 == 0) / 2).is_integer()
#         i += 1
#     return _sum

# def count_consecutive_summers(num):
#     count = 0
#     array = [x for x in range(1,num+1)]
#     for start in range(num):
#         for end in range(start,num+1):
#             if sum(array[start:end]) == num:
#                 count += 1
#                 print array[start:end]
#     return count
#
# print count_consecutive_summers(105)


