# @Time    : 2021/8/12 14:10
# @Author  : lucas
# @File    : 1.py
# @Project : locust demo
# @Software: PyCharm



def max_sub_array(nums) -> int:
    sum_ = nums[0]
    for i in range(1, len(nums)):
        sum_ = max(nums[i] + sum_, nums[i])
        if sum_ > nums[i]:
            nums[i] = sum_
    return max(nums)

num = [-2,1,-3,4,-1,2,1,-5,4]
print(max_sub_array(num))