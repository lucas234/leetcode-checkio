# @Time    : 2021/8/12 16:20
# @Author  : lucas
# @File    : 88.Merge_Sorted_Array.py
# @Project : locust demo
# @Software: PyCharm


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
for index, i in enumerate(nums2):
    count = 0
    while count < len(nums1):
        if i < nums1[count]:
            nums1.pop(-1)
            nums1.insert(count, i)
            break
        else:
            count += 1
    if count == len(nums1):
        s = n - index
        for j in nums2[index:]:
            nums1[-s] = j
            s -= 1
        break

print(nums1)


