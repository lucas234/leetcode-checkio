# @Time    : 2020/8/17 15:42
# @Author  : lucas
# @File    : 14.Longest_Common_Prefix.py
# @Project : locust demo
# @Software: PyCharm
from typing import List


# def longest_common_prefix(strs: List[str]) -> str:
#     if not strs:
#         return ""
#     count = 0
#     result = ""
#     longest_common_prefix = min([len(j) for j in strs])
#     while count < longest_common_prefix:
#         count += 1
#         common_prefix = [i[0] if len(i) == 1 else i[0:count] for i in strs]
#         if len(set(common_prefix)) == 1:
#             result = strs[0][0:count] if len(strs[0]) != 1 else strs[0][0]
#     return result
#
#
# strs = ["flower","flow","flight"]
# print(longest_common_prefix(strs))



def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ""
    s1, s2 = min(strs), max(strs)
    i = 0
    while i < len(s1) and i < len(s2) and s1[i] == s2[i]:
        i += 1
    return s1[:i]


strs = ["flower","flow","flight","fw"]
print(longestCommonPrefix(strs))