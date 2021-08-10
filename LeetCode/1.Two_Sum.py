# @Time    : 2021/7/6 15:23
# @Author  : lucas
# @File    : 1.Two_Sum.py
# @Project : locust demo
# @Software: PyCharm
from typing import List


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    d = {}
    for idx, num in enumerate(nums):
        remain = target - num
        if remain in d:
            return [d[remain], idx]
        else:
            d[num] = idx

nums = [3,3]
print(twoSum(nums, 6))