# @Time    : 2021/7/9 17:35
# @Author  : lucas
# @File    : 27.Remove_Element.py
# @Project : locust demo
# @Software: PyCharm
from typing import List


def remove_element(nums: List[int], val: int) -> int:
    count = 0
    while count < len(nums):
        if nums[count] == val:
            nums.remove(val)
        else:
            count += 1
    return count


nums = [0, 1, 2, 2, 3, 0, 4, 2]
print(remove_element(nums, 2))
