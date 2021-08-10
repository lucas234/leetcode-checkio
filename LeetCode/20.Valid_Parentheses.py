# @Time    : 2021/7/8 10:49
# @Author  : lucas
# @File    : 20.Valid_Parentheses.py
# @Project : locust demo
# @Software: PyCharm


def is_valid(s):
    parentheses = {"(": ")", "{": "}", "[": "]"}
    stack = list()
    left = parentheses.keys()
    right = parentheses.values()
    for i in s:
        if i in left:
            stack.append(i)
        if i in right:
            if stack and parentheses[stack[-1]] == i:
                stack.pop()
            else:
                return False
    if not stack:
        return True


print(is_valid("]]"))
print(is_valid("()[]{}"))
print(is_valid("()"))
print(is_valid("(]"))
print(is_valid("([)]"))
print(is_valid("{[]}"))
