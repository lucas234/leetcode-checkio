# coding=utf-8
# auther：Liul5
# date：2019/5/13 9:33
# tools：PyCharm
# Python：2.7.15
# https://py.checkio.org/en/mission/keys-and-locks/


def remove_redundant(_string):
    _string = _string.split()
    coordinate = [(index1, index2) for index1, i in enumerate(_string) for index2, j in enumerate(i) if j == "#"]
    x, y = [i for i in zip(*coordinate)]
    _string = _string[min(x):max(x)+1]
    _string = [i[min(y):max(y)+1] for i in _string]
    return _string


def rotated(_list):
    _list90 = ["".join(reversed(i)) for i in zip(*_list)]
    _list180 = ["".join(reversed(i)) for i in zip(*_list90)]
    _list270 = ["".join(reversed(i)) for i in zip(*_list180)]
    return [_list, _list90, _list180, _list270]


def keys_and_locks(key_string, lock_string):
    key = remove_redundant(key_string)
    lock = remove_redundant(lock_string)
    if sorted([len(key), len(key[0])]) != sorted([len(lock), len(lock[0])]):
        return False
    keys = rotated(key)
    if lock in keys:
        return True
    return False


print keys_and_locks('''
0##0
0##0
00#0
00##
00##''',
'''
00000
000##
#####
##000
00000''') == True

