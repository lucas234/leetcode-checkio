# auther：Liul8
# date：2020/3/31 16:21
# tools：PyCharm
# Python：3.7.7
# https://py.checkio.org/en/mission/even-last/


def checkio(items: list) -> int:
    if not items:
        return 0
    even_list = items[::2]
    return sum(even_list) * items[-1]


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio([0, 1, 2, 3, 4, 5]))

    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

