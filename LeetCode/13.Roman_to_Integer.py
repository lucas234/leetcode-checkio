# @Time    : 2020/8/17 9:50
# @Author  : lucas
# @File    : 13.Roman_to_Integer.py
# @Project : locust demo
# @Software: PyCharm


def roman_to_int(s: str) -> int:
    mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000,
               "Q": 900, "R": 90, "S": 4, "T": 9, "U": 400, "W": 40}
    result = s.replace("CM", "Q").replace("XC", "R").replace("IV", "S").replace("IX", "T").replace("CD", "U").replace(
        "XL", "W")
    num = 0
    for i in result:
        num += int(mapping[i])
    return num


