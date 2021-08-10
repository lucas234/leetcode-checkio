# @Time    : 2021/7/6 16:43
# @Author  : lucas
# @File    : 204.Count_Primes.py
# @Project : locust demo
# @Software: PyCharm
from math import sqrt


def is_primes1(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def is_primes2(n):
    if n > 1:
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for x in range(3, int(sqrt(n) + 1), 2):
            if n % x == 0:
                return False
        return True
    return False

# print(is_primes2(17))

def count_primes(n):
    if n < 2:
        return 0
    s = [1] * n
    s[0] = s[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            for j in range(i * i, n, i):
                s[j] = 0
            # s[i * i: n: i] = [0] * (1 + (n - i * i - 1) // i)
    return sum(s)

print(count_primes(1113))
