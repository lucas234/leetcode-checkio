# @Time    : 2021/7/9 16:35
# @Author  : lucas
# @File    : 26.Remove_Duplicates_From_Sorted_Array.py
# @Project : locust demo
# @Software: PyCharm
from typing import List


def remove_duplicates(nums:List[int])->int:
    count = 0
    while count+1 < len(nums):
        if nums[count] == nums[count+1]:
            nums.remove(nums[count+1])
        else:
            count += 1
    return len(nums)

a = [0,0,1,1,1,2,2,3,3,4]
print(remove_duplicates(a))