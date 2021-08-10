# coding=utf-8
# auther：Liul5
# date：2019/3/28 9:17
# tools：PyCharm
# Python：2.7.15


def fibonacci(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
        yield a
# def fibonacci1(n):
#     if n <= 1:
#         return 1
#     else:
#         return fibonacci1(n-1) + fibonacci1(n-2)
# print fibonacci1(0)


# print list(fibonacci(100))[:20]


def checkio(_opacity):
    opacity = 10000
    opacity_age = {opacity: 0}
    for i in range(1, 5000):
        if i in list(fibonacci(100))[:20]:
            opacity -= i
        else:
            opacity += 1
        opacity_age[opacity] = i
    return opacity_age.get(_opacity)

# def checkio1(B00):
#     BO0, B0O, BOO = 1, 1, 0
#     while B00 != 10000:
#         BOO += 1
#         if BOO == B0O:
#             B00 += B0O
#             BO0, B0O = B0O, BO0+B0O
#         else:
#             B00 -= 1
#     return BOO


# list 去重
# ids = [1,4,3,3,4,2,3,4,5,6,1]
# func = lambda x,y:x if y in x else x + [y]
# print reduce(func, ids, [])

from math import sqrt

def isSqr(x):
    return x == int(sqrt(x)) ** 2

def isFib(x):
    return isSqr(5 * x*x + 4) or isSqr(5 * x*x - 4)

def checkio(opacity):
    c = 10000
    x = 0
    while(1):
        c -= x if isFib(x) else -1
        if c == opacity:
            return x
        x += 1