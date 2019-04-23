# coding=utf-8
# auther：Liul5
# date：2019/4/22 13:51
# tools：PyCharm
# Python：2.7.15
# 参考：https://www.mathwarehouse.com/probability/permutations-repeated-items.php
# 参考：https://medium.com/ken-m-lai/walkthrough-of-probably-dice-f01a1bf79c77
# https://py.checkio.org/en/mission/probably-dice/
from __future__ import division


def probability(dice_number, side, target):
    # sides = [range(1, side + 1)] * dice_number
    # # all_combinations = product(*sides)
    # all_totallings = filter(lambda x: sum(x) == target, product(*sides))
    # return round(len(all_totallings) / side ** dice_number, 4)
    from math import factorial
    from collections import Counter
    from itertools import combinations_with_replacement
    count = 0
    for i in combinations_with_replacement(range(1, side + 1), dice_number):
        if sum(i) == target:
            # print Counter(i)
            count += factorial(len(i)) / reduce(lambda x, y: x * y, map(factorial, Counter(i).values()))
    return round(count / side ** dice_number, 4)


print probability(2, 6, 3)  # == 0.0556  # 2 six-sided dice have a 5.56% chance of totalling 3
print probability(2, 6, 4)  # == 0.0833
print probability(2, 6, 7)  # == 0.1667
print probability(2, 3, 5)  # == 0.2222  # 2 three-sided dice have a 22.22% chance of totalling 5
print probability(2, 3, 7)  # == 0       # The maximum you can roll on 2 three-sided dice is 6
print probability(3, 6, 7)  # == 0.0694
print probability(10, 10, 50)  # == 0.0375


# python3
# def probability(dice_number, side, target):
#     from math import factorial
#     from collections import Counter
#     from itertools import combinations_with_replacement
#     from functools import reduce
#     count = 0
#     for i in combinations_with_replacement(range(1, side + 1), dice_number):
#         if sum(i) == target:
#             # print Counter(i)
#             count += factorial(len(i)) / reduce(lambda x, y: x * y, map(factorial, Counter(i).values()))
#     return round(count / side ** dice_number, 4)
