# @Time    : 2021/7/23 15:47
# @Author  : lucas
# @File    : 35.Search_Insert_Position.py
# @Project : locust demo
# @Software: PyCharm
from typing import List


def search_insert(nums: List[int], target: int) -> int:
    for i, v in enumerate(nums):
        if v >= target:
            return i
    return len(nums)


# Input: nums = [1,3,5,6], target = 7
# Output: 4