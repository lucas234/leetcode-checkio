# @Time    : 2021/7/23 16:21
# @Author  : lucas
# @File    : 67.Add_Binary.py
# @Project : locust demo
# @Software: PyCharm


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2)+int(b, 2))[2:]