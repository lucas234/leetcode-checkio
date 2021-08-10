# coding=utf-8
# auther：Liul5
# date：2019/3/26 9:20
# tools：PyCharm
# Python：2.7.15
# 求最大值的单词
# e, a, i, o, n, r, t, l, s, u = 1
# d, g = 2
# b, c, m, p = 3
# f, h, v, w, y = 4
# k = 5
# j, x = 8
# q, z = 10
# 例子
#  'dog' 是 5, 因为 'd' = 2, 'o' = 1 和 'g' = 2
# worth_of_words(['hi', 'quiz', 'bomb', 'president']) == 'quiz'
# worth_of_words(['zero', 'one', 'two', 'three', 'four', 'five']) == 'zero'

VALUES = {'a': 1, 'c': 3, 'b': 3, 'e': 1, 'd': 2, 'g': 2, 'f': 4, 'i': 1,
          'h': 4, 'k': 5, 'j': 8, 'm': 3, 'l': 1, 'o': 1, 'n': 1, 'q': 10,
          'p': 3, 's': 1, 'r': 1, 'u': 1, 't': 1, 'w': 4, 'v': 4, 'y': 4,
          'x': 8, 'z': 10}


def worth_of_words(words_list):
     _max = max([sum(map(VALUES.get, list(i))) for i in words_list])
     _index = [sum(map(VALUES.get, list(i))) for i in words_list].index(_max)
     return words_list[_index]


print worth_of_words(['hi', 'quiz', 'bomb', 'president']) == 'quiz'
print worth_of_words(['zero', 'one', 'two', 'three', 'four', 'five']) == 'zero'



# def worth_of_words(words):
#     return max(words, key=lambda w: sum((VALUES[c] for c in w)))

# print " ".join([i.capitalize() if j in [0, len(worth_of_words.__name__.split("_")) - 1] else i for j, i in enumerate(worth_of_words.__name__.split("_"))])