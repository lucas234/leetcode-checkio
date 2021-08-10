# @Time    : 2020/8/14 15:21
# @Author  : lucas
# @File    : Container_With_Most_Water.py
# @Project : locust demo
# @Software: PyCharm

# height = [159,157,139,51,98,71,4,125,48,125,64,4,105,79,136,169,113,13,95,88,190,5,148,17,152,20,196,141,35,42,188,147,199,127,198,49,150,154,175,199,80,191,3,137,22,92,58,87,57,153,175,199,110,75,16,62,96,12,3,83,55,144,30,6,23,28,56,174,183,183,173,15,126,128,104,148,172,163,35,181,68,162,181,179,37,197,193,85,10,197,169,17,141,199,175,164,180,183,90,115]
# height = [1,2]
# length = len(height)
# right_max_area = 0
# left_max_area = 0
# for index in range(0,length):
#     # if height[index]
#     right_point = length - 1
#     left_point = 0
#     while left_point < index:
#         if height[left_point] < height[index]:
#             left_point += 1
#         else:
#             left_max_area = max((index - left_point) * height[index], left_max_area)
#             break
#     while index < right_point :
#         if height[index] > height[right_point]:
#             right_point -= 1
#         else:
#             right_max_area = max((right_point - index) * height[index], right_max_area)
#             break
#
#     # print(index, height[index])
# print(max(right_max_area, left_max_area))


height =  [1,8,6,2,5,4,8,3,7]

from typing import List

def max_area(height: List[int]) -> int:
    length = len(height)
    l, r = 0, length - 1
    max_area = 0
    while l < r:
        max_area = max(min(height[l], height[r]) * (r - l), max_area)
        if height[l] > height[r]:
            r -= 1
        else:
            l += 1
    return max_area

print(max_area(height))
