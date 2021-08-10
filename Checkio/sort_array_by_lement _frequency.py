# coding=utf-8
# auther：Liul5
# date：2019/3/22 9:44
# tools：PyCharm
# Python：2.7.15
# 列表按照元素出现的频率排序
# 1.按照元素出现的频率降序排列
# 2.如果频率相同的元素，则按照元素第一次出现的索引排序
# 输入：Iterable
# 输出: Iterable
# 例子:
# frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]) == [4, 4, 4, 4, 6, 6, 2, 2]
# frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob']) == ['bob', 'bob', 'bob', 'carl', 'alex']
from functools import reduce


def frequency_sort(_list):
    if not _list:
        return _list
    times_index = {i: (_list.count(i), _list.index(i)) for i in _list}
    after_sort = sorted(times_index.items(), key=lambda x: (-x[1][0], x[1][1]))
    times = [[i[0]] * i[1][0] for i in after_sort]
    return reduce(lambda x, y: x + y, times)


print frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]) == [4, 4, 4, 4, 6, 6, 2, 2]
print frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob']) == ['bob', 'bob', 'bob', 'carl', 'alex']
print frequency_sort([]) == []

# import collections
#
# def frequency_sort(items):
#     counted = collections.Counter(items).most_common()
#
#     ret=[]
#     for key, freq in counted:
#         ret.extend([key for c in range(freq)])
#     return ret

# def frequency_sort1(items):
#     result=[]
#     sort_items = sorted([(items.index(i),items.count(i)) for i in items], key = lambda x : (-x[1],x[0]))
#     for i in sort_items:
#         print items[i[0]]
#         result.append(items[i[0]])
#     return result
# print frequency_sort1(['bob', 'bob', 'carl', 'alex', 'bob'])


# import operator
# import collections
#
# def frequency_sort(items):
#     collect = collections.OrderedDict()
#
#     for item in items:
#         if item in collect:
#             collect[item] += 1
#         else:
#             collect[item] = 1
#
#     # отсортировали
#     sort = sorted(collect.items(), key=operator.itemgetter(1), reverse=True)
#     result = list()
#
#     # собрали результат
#     for i in sort:
#         for m in range(i[1]):
#             result.append(i[0])
#     return result

# 例如使用itemgetter()从元组记录中取回特定的字段：
# from operator import itemgetter
# inventory = [('apple', 3), ('banana', 2), ('pear', 5), ('orange', 1)]
# getcount = itemgetter(1)
# print list(map(getcount, inventory))
# #[3, 2, 5,1]
# print sorted(inventory, key=getcount)
# #[('orange',1), ('banana', 2), ('apple', 3), ('pear', 5)]