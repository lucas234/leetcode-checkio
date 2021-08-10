# auther：Liul8
# date：2020/3/31
# tools：PyCharm
# Python：3.7.7
# https://py.checkio.org/en/mission/sum-numbers/


def sum_numbers(text: str) -> int:
    # your code here
    str_list = text.split(" ")
    num_list = [int(i) for i in str_list if i.isdigit()]
    return sum(num_list) if num_list else 0


if __name__ == '__main__':
    print("Example:")
    print(sum_numbers('hi'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sum_numbers('hi') == 0
    assert sum_numbers('who is 1st here') == 0
    assert sum_numbers('my numbers is 2') == 2
    assert sum_numbers('This picture is an oil on canvas '
 'painting by Danish artist Anna '
 'Petersen between 1845 and 1910 year') == 3755
    assert sum_numbers('5 plus 6 is') == 11
    assert sum_numbers('') == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")
