# @Time    : 2020/8/18 10:45
# @Author  : lucas
# @File    : 5.Longest_Palindromic_Substring.py
# @Project : locust demo
# @Software: PyCharm


def longest_palindrome(s: str) -> str:
    palindrome = ""
    for i in range(len(s)):
        for j in range(len(s), i, -1):
            if len(palindrome) >= j - i:
                break
            if s[i:j] == s[i:j][::-1]:
                palindrome = s[i:j]
                break
    return palindrome

