# @Time    : 2021/7/15 9:22
# @Author  : lucas
# @File    : 485.Max_Consecutive_Ones.py
# @Project : locust demo
# @Software: PyCharm
from typing import  List


def find_max_consecutive_ones(nums: List[int]) -> int:
    count = 0
    max_num = 0
    for i, value in enumerate(nums):
        if value == 1:
            count += 1
        else:
            max_num = max(max_num, count)
            count = 0
    max_num = max(max_num, count)
    return max_num


def find_max_consecutive_nums(nums: List[int]) -> int:
    count = 0
    max_num = 0
    start = nums[0]
    for i, value in enumerate(nums):
        if value == start:
            count += 1
        else:
            max_num = max(max_num, count)
            start = value
            count = 1
    max_num = max(max_num, count)
    return max_num


nums = [1,1,0,1,1,1]
print(find_max_consecutive_nums(nums))
print(find_max_consecutive_ones(nums))