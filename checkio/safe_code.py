# coding=utf-8
# auther：Liul5
# date：2019/5/14 9:30
# tools：PyCharm
# Python：2.7.15
# https://py.checkio.org/en/mission/safe-code/
import re


def parse_string(code):
    previous, result = code.split("=")
    if "*" in previous:
        index = previous.find("*")
        return previous[:index], "*", previous[index + 1:], result
    if "+" in previous:
        index = previous.find("+")
        return previous[:index], "+", previous[index + 1:], result
    if "-" in previous:
        if previous[0] != "-":
            index = previous.find("-")
            return previous[:index], "-", previous[index + 1:], result
        else:
            index = previous[1:].find("-")
            return previous[:index + 1], "-", previous[index + 2:], result


def safe_code(code):
    equation_nums = set(int(i) for i in re.findall("\d", code))
    nums = set(range(10)).difference(equation_nums)
    first, sign, second, result = parse_string(code)
    for i in nums:
        first_num = first.replace("#", str(i))
        second_num = second.replace("#", str(i))
        results = result.replace("#", str(i))
        if first_num[0] != "0" and second_num[0] != "0" and results[0] != "0":
            if sign == "*":
                if int(first_num) * int(second_num) == int(results):
                    return i
            if sign == "-":
                if int(first_num) - int(second_num) == int(results):
                    return i
            if sign == "+":
                if int(first_num) + int(second_num) == int(results):
                    return i
    return -1


print safe_code("-5#*-1=5#") == 0
print safe_code("##*##=302#") == 5
print safe_code("19--45=5#") == -1
print safe_code("#9+3=12") == -1
print safe_code("24-35=-##")
print safe_code("11*#=##")
print safe_code("#*11=##")



# def safe_code(equation):
#     equation = equation.replace('=', '==')
#     digits = ('' if '##' in equation else '0') + '123456789'
#     for digit in digits:
#         if digit not in equation:
#             try:
#                 if eval(equation.replace('#', digit)):
#                     return int(digit)
#             except:
#                 pass
#     return -1
#
# print safe_code("19--45=5#")