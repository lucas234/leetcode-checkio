# auther：Liul8
# date：2020/4/8 16:59
# tools：PyCharm
# Python：3.7.7
# https://py.checkio.org/en/mission/second-index/


def second_index(text: str, symbol: str) -> [int, None]:
    count = 0
    for index, value in enumerate(text):
        if value == symbol:
            count += 1
        if count == 2:
            return index
    return None


if __name__ == '__main__':
    print('Example:')
    print(second_index("sims", "s"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert second_index("sims", "s") == 3, "First"
    assert second_index("find the river", "e") == 12, "Second"
    assert second_index("hi", " ") is None, "Third"
    assert second_index("hi mayor", " ") is None, "Fourth"
    assert second_index("hi mr Mayor", " ") == 5, "Fifth"
    print('You are awesome! All tests are done! Go Check it!')
