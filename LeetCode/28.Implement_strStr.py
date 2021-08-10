# @Time    : 2021/7/23 15:49
# @Author  : lucas
# @File    : 28.Implement_strStr.py
# @Project : locust demo
# @Software: PyCharm


def strStr(haystack: str, needle: str) -> int:
    if needle in haystack:
        return haystack.index(needle)
    else:
        return -1

# Input: haystack = "hello", needle = "ll"
# Output: 2