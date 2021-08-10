# @Time    : 2021/7/7 15:25
# @Author  : lucas
# @File    : 202.Happy_Number.py
# @Project : locust demo
# @Software: PyCharm


def is_happy(n):
    if n == 1:
        return True
    nums = [n]
    while n != 1:
        # num_sums = 0
        num_sums = sum([int(i) ** 2 for i in str(n)])
        # for i in str(n):
        #     sum += int(i) ** 2
        if num_sums in nums:
            return False
        nums.append(num_sums)
        n = int(num_sums)
    return True

print(is_happy(19))