# @Time    : 2021/7/27 10:06
# @Author  : lucas
# @File    : 66.Plus_One.py
# @Project : locust demo
# @Software: PyCharm
from typing import List


def plus_one(digits: List[int]) -> List[int]:
    num = "".join([str(i) for i in digits])
    print(num)
    result = str(int(num) + 1)
    return list(result)


nums = [1, 2, 3]
print(plus_one(nums))
