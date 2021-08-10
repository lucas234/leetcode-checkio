# coding=utf-8
# auther：Liul5
# date：2019/5/9 14:02
# tools：PyCharm
# Python：2.7.15
# https://py.checkio.org/en/mission/brackets/


def checkio(_string):
    map_brackets = {"{": "}", "[": "]", "(": ")"}
    left = map_brackets.keys()
    right = map_brackets.values()
    result = []
    for i in _string:
        if i in left:
            result.append(i)
        if i in right:
            if not result:
                return False
            if map_brackets.get(result[-1]) == i:
                result.pop()
            else:
                return False
    return result == []


print checkio("((5+3)*2+1)") == True
print checkio("{[(3+1)+2]+}") == True
print checkio("(3+{1-1)}") == False
print checkio("[1+1]+(2*2)-{3/3}") == True
print checkio("(({[(((1)-2)+3)-3]/3}-3)") == False
print checkio("2+3") == True

# def checkio(expression):
#     brackets = {'(':')', '[':']', '{':'}'}
#
#     stack = []
#     for char in expression:
#         if char in brackets:
#             stack.append(char)
#         if char in brackets.values():
#             if not stack:
#                 return False
#             if char != brackets[stack.pop()]:
#                 return False
#
#     return not stack
