# auther：Liul8
# date：2020/5/13 14:16
# tools：PyCharm
# Python：3.7.7

from itertools import product, permutations, combinations

#
# def two_sum(nums, target):
#     """
#     :type nums: List[int]
#     :type target: int
#     :rtype: List[int]
#     """
#     d = {}
#     for idx, num in enumerate(nums):
#         remain = target - num
#         if remain in d:
#             return [d[remain], idx]
#         if remain not in d:
#             d[num] = idx
#         print(d)
#
#
# # print(two_sum([2,5,5,11],10))

# nums = [-5, 10, 99, 123456]


# def is_ascending(items: list) -> bool:
#     # your code here
#     # if not items:
#     #     return True
#     for k in range(len(items) - 1):
#         if items[k + 1] <= items[k]:
#             return False
#     return True


# print(is_ascending(nums))

# num = [-1, 0, 1, 2, -1, -4]
#
#
# def threeSum(nums):
#     res = []
#     nums.sort()
#     length = len(nums)
#     for i in range(length - 2):  # [8]
#         if nums[i] > 0: break  # [7]
#         if i > 0 and nums[i] == nums[i - 1]: continue  # [1]
#
#         l, r = i + 1, length - 1  # [2]
#         while l < r:
#             total = nums[i] + nums[l] + nums[r]
#
#             if total < 0:  # [3]
#                 l += 1
#             elif total > 0:  # [4]
#                 r -= 1
#             else:  # [5]
#                 res.append([nums[i], nums[l], nums[r]])
#                 while l < r and nums[l] == nums[l + 1]:  # [6]
#                     l += 1
#                 while l < r and nums[r] == nums[r - 1]:  # [6]
#                     r -= 1
#                 l += 1
#                 r -= 1
#     return res
#
# print(threeSum(num))


# s = "abcabcbb"
# s = "anviaj"
# longest = ""
# for i in range(len(s)):
#     sub = s[i:]
#     for j in range(len(sub)):
#         if sub[j] in sub[:j]:
#             if len(longest) < len(sub[:j]):
#                 longest = sub[:j]
#             break
#         else:
#             if len(longest) < len(sub[:j+1]):
#                 longest = sub[:j+1]
#
# print(longest)


# def lengthOfLongestSubstring(s):
#     """
#     :type s: str
#     :rtype: int
#     """
#     mapping = dict()
#     max_length = 0
#     start = 0
#     for index in range(len(s)):
#         if s[index] in mapping.keys():
#             if mapping[s[index]] >= start:
#                 max_length = max(max_length, index - start)
#                 start = mapping[s[index]] + 1
#         mapping[s[index]] = index
#     return max(max_length, len(s) - start)

# def lengthOfLongestSubstring(s: str) -> int:
#     maxlen, ss, p = 0, 0, 0
#     _set = set()
#     while p < len(s):
#         if not s[p] in _set:
#             _set.add(s[p])
#             p += 1  # point a next element
#             maxlen = max(maxlen, len(_set))
#         else:
#             _set.remove(s[ss])  # should remove first character to move to the next element
#             ss += 1  # move the starting pointer to the next element
#         print(p, _set)
#
#     return maxlen

def lengthOfLongestSubstring(s: str) -> int:
    sub = ""
    max_len = 0
    for ch in s:
        if ch in sub:
            if max_len < len(sub):
                max_len = len(sub)
            index = sub.index(ch)
            sub += ch
            sub = sub[index+1:]
        else:
            sub += ch
    return max(max_len, len(sub))
# print(lengthOfLongestSubstring("abcacc"))


# def lengthOfLongestSubstring(s: str) -> int:
#     b = ''
#     l = ''
#     for c in s:
#         if c in b:
#             i = b.index(c)
#             b = b[i + 1:] + c
#         else:
#             b += c
#             if len(b) > len(l):
#                 l = b
#     return len(l)

nums1 = [1, 2]
nums2 = [3,4]

i = 0
j = 0
sort_list = []
while i < len(nums1) and j < len(nums2):
    if nums1[i] > nums2[j]:
        sort_list.append(nums2[j])
        j += 1
    else:
        sort_list.append(nums1[i])
        i += 1


all_ = sort_list+nums1[i:]+nums2[j:]
print(all_)
mid = len(all_) // 2
if len(all_) & 1:
    print(all_[mid])
else:
    print((all_[mid]+all_[mid-1]) / 2)