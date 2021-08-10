# auther：Liul8
# date：2020/3/31 15:06
# tools：PyCharm
# Python：3.7.7
# https://py.checkio.org/en/mission/split-list/


def split_list(array_list: list)->list:
    length = len(array_list)
    if length == 0:
        return [[], []]
    if divmod(length, 2)[1] != 0:
        return [array_list[:length // 2 + 1], array_list[length // 2 + 1:]]
    else:
        return [array_list[:length // 2], array_list[length // 2:]]


if __name__ == '__main__':
    print("Example:")
    print(split_list([1, 2, 3, 4, 5, 6]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
    assert split_list([1, 2, 3]) == [[1, 2], [3]]
    assert split_list([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]
    assert split_list([1]) == [[1], []]
    assert split_list([]) == [[], []]
    print("Coding complete? Click 'Check' to earn cool rewards!")


# best solutions

# def split_list(items: list) -> list:
#     # your code here
#     # python 3.8 海象运算符 :=
#     return [items[:(mid := (len(items) + 1)//2)], items[mid:]]