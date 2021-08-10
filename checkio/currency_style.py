# coding=utf-8
# auther：Liul5
# date：2019/5/8 16:29
# tools：PyCharm
# Python：2.7.15
# https://py.checkio.org/en/mission/currency-style/
import re


def func(m):
    r = m.group(0)
    if len(r) >= 3 and r[-3] in [",", "."]:
        r = r[:-3]+"++"+r[-2:]
    return r.replace(".", ",")


def checkio(args):
    if args[-1] == ".":
        _str = "."
        args = args[:-1]
    else:
        _str = ""
    p = re.compile(r"\$[\d.,]+")
    return p.sub(func, args).replace("++", ".") + _str


print checkio("Lot 192.001 costs $1.000,94.") == "Lot 192.001 costs $1,000.94."
print checkio("$1,23 + $2,34 = $3,57.") == "$1.23 + $2.34 = $3.57."
print checkio("$8.000 - $8.000 = $0")


# def checkio(text):
#     "Convert Euro style currency in dollars to US/UK style"
#     import string
#     table = string.maketrans(',.', '.,')
#
#     def restyle(match):
#         return match.group().translate(table)
#
#     return re.sub(r'\$\d{1,3}(\.\d{3})*(,\d{1,2})?\b', restyle, text)
