# @Time    : 2021/7/27 9:39
# @Author  : lucas
# @File    : 69.Sqrt(x).py
# @Project : locust demo
# @Software: PyCharm


def my_sqrt(x: int) -> int:
    if x == 1: return 1
    for i in range(int(x / 2) + 1):
        if i * i == x:
            return i
        if i * i > x:
            return i - 1
    return i


print(my_sqrt(2))


# class Solution:
#     def mySqrt(self, x: int) -> int:
#         low = 0
#         high = x
#         while low <= high:
#             mid = low + (high - low) // 2
#             if mid * mid == x:
#                 return mid
#             elif mid * mid < x:
#                 ans = mid
#                 low = mid + 1
#             else:
#                 high = mid - 1
#         return ans