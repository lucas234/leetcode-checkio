# @Time    : 2021/8/12 14:37
# @Author  : lucas
# @File    : 70.Climbing_Stairs.py
# @Project : locust demo
# @Software: PyCharm


def climb_stairs(n: int) -> int:
    if n <= 2: return n
    first, second = 1, 2
    for i in range(2, n):
        first, second = second, first+second
    return second

print(climb_stairs(3))