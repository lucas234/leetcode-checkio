# @Time    : 2020/8/12 9:21
# @Author  : lucas
# @File    : Palindrome_Number.py
# @Project : locust demo
# @Software: PyCharm

def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    result = str(x)[::-1]
    return int(result) == x
