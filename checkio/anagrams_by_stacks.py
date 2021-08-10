# coding=utf-8
# auther：Liul5
# date：2019/4/30 15:35
# tools：PyCharm
# Python：2.7.15
# https://py.checkio.org/en/mission/anagrams-by-stacks/
import Queue
import copy


def checkio(_str):
    original, anagrams = _str.split("-")
    original = list(original)
    b = copy.copy(original)
    original.reverse()
    a = original
    o = list(anagrams)
    # o = ['t', 'r', 'o', 't']  # ['c', 'i', 'r', 'e']
    # a = ['t', 'r', 'o', 't']  # ['e', 'c', 'i', 'r']
    # b = ['t', 'o', 'r', 't']  # ['r', 'i', 'c', 'e']
    s = []
    t = []
    z = []
    result = ""
    for j in a:
        if j == o[len(t)]:
            if b:
                z.append(b.pop())
                result += "10,"
            if s:
                for k in s[len(t):]:
                    b.append(k)
                    result += "21,"
            if z:
                t.append(z.pop(0))
                result += "02,"
        else:
            if b:
                s.append(b.pop())
                result += "12,"
    return result[:-1]

# print checkio("rice-cire") == "10,12,12,12,02"
# print checkio("tort-trot") == "12,12,12,12"
# print checkio("hello-holle") == "12,12,12,12,10,21,21,21,21,02,12,12,12,12"
# print checkio("anagram-mragana") == "12,10,12,02,12,12,12,12"
# print checkio("mirror-mirorr") == "12,12,10,12,12,02,10,21,21,21,21,21,02,12,12,12,10,21,21,21,02,12,12,12,12"



_str = "rice-cire"
original, anagrams = _str.split("-")
print original
original = list(original)
original.reverse()
print original
result = ""
size = len(original)
first = Queue.Queue(size)
second = Queue.Queue(size)
third = Queue.Queue(size)
zero = Queue.Queue(1)
for i in original:
    first.put(i)
result = ""

o = ['t', 'r', 'o', 't']#['c', 'i', 'r', 'e']
a = ['t', 'r', 'o', 't']#['e', 'c', 'i', 'r']
b = ['t', 'o', 'r', 't']#['r', 'i', 'c', 'e']
s = []
t = []
z = []

for j in a:
    if j == o[len(t)]:
        if b:
            z.append(b.pop())
            result += "10, "
        if s:
            for k in s[len(t):]:
                b.append(k)
                result += "21, "
        if z:
            t.append(z.pop(0))
            result += "02, "
    else:
        if b:
            s.append(b.pop())
            result += "12, "
print result
print checkio("tort-trot")