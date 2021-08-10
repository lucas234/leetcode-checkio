# auther：Liul8
# date：2020/4/8 14:35
# tools：PyCharm
# Python：3.7.7
# https://py.checkio.org/en/mission/digits-multiplication/


def checkio(number: int) -> int:
    from functools import reduce
    return int(reduce(lambda x, y: int(x) * int(y), filter(lambda x: int(x) * 1 != 0, str(number))))


if __name__ == '__main__':
    print('Example:')
    print(checkio(123405))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

# number = 123054
# accumulate = 1
# for i in str(number):
#     if int(i):
#         accumulate *= int(i)
# print(accumulate)

