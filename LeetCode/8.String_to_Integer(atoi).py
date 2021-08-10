# @Time    : 2020/8/12 9:51
# @Author  : lucas
# @File    : String_to_Integer(atoi).py
# @Project : locust demo
# @Software: PyCharm


def myAtoi(str: str) -> int:
    """my solution"""
    import re
    str = str.strip()
    result = re.search("\d+", str)
    if result and str.index(result[0])==0:
        num = int(result[0])
    elif result and str.index(result[0]) ==1 and str[0] in ["-", "+"]:
        num = int(str[0]+result[0])
    else:
        num = 0
    if -pow(2, 31) > num:
        return -pow(2, 31)
    if pow(2, 31) - 1 < num:
        return pow(2, 31) - 1
    return num


def myAtoi1(s: str) -> int:
    """best solution"""
    import re
    s = s.strip().lstrip()
    s = re.match('[+-]?\d+', s)

    if s:
        s = int(s.group())
        print(s)
    else:
        return 0

    if s <= -2 ** 31: return -2 ** 31
    if s >= 2 ** 31: return (2 ** 31) - 1
    return s

print(myAtoi1("+-1"))
