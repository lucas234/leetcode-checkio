# @Time    : 2021/7/23 16:06
# @Author  : lucas
# @File    : 58.Length_of_Last_Word.py
# @Project : locust demo
# @Software: PyCharm


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(" ")[-1])