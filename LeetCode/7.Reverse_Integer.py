# @Time    : 2020/8/11 13:55
# @Author  : lucas
# @File    : Reverse_Integer.py
# @Project : locust demo
# @Software: PyCharm

def reverse_integer(x:int)->int:
    if x < 0:
        result =  -int(str(x)[1:][::-1])
    else:
        result =  int(str(x)[::-1])
    return result if -pow(2, 31) < result < pow(2, 31) - 1 else 0



