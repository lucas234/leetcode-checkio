# coding=utf-8
# 作者：Liul5
# 日期：2019/3/19 9:30
# 工具：PyCharm
# Python：2.7.15
#
# https://py.checkio.org/en/mission/flatten-list/
# 将嵌套的列表输出成一个列表，包含所有元素
# 输入: 一个嵌套的整形列表.
# 输出: 一个单一的整形列表.
# 例子:
# flat_list([1, 2, 3]) == [1, 2, 3]
# flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4]
# flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7]
# flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1]


import re


def flat_list(_list):
    pattern = re.compile("(-\d{1,}|\d{1,}).*?")
    return list(map(int, re.findall(pattern, """%s""" % _list)))


print flat_list([100, 2, 3])
print flat_list([1, 2, 3]) == [1, 2, 3]
print flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4]
print flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7]
print flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1]

#first

# def flat_list1(array):
#     import re
#     return [int(number) for number in re.findall(r"[0-9-]+", str(array))]

#second
# def flat_list2(array, a=None):
#     if a is None:
#         a = []
#     for i in array:
#         if isinstance(i, list):
#             flat_list(i, a)
#         else:
#             a.append(i)
#     return a

# def flat_list2(array):
#     result = []
#     for item in array:
#         if isinstance(item, int):
#             result.append(item)
#         else:
#             result += flat_list(item)
#
#     return result

#third
# def flat_list(array):
#     if not array: return []
#     head, *array = array
#     if not type(head) == list: return [head] + flat_list(array)
#     return flat_list(head) + flat_list(array)


# def flat_list(array):
#     return [int(x) for x in (str(array).replace('[', '').replace(']', '').split(', ')) if x != '']



# def flat_list(a):
#     return sum(([x] if not isinstance(x, list) else flat_list(x)
#              for x in a),[])

