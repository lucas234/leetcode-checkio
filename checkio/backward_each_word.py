# auther：Liul8
# date：2020/4/8 13:32
# tools：PyCharm
# Python：3.7.7
# https://py.checkio.org/en/mission/backward-each-word/


def backward_string_by_word(text: str) -> str:
    # your code here
    if not text:
        return ""
    return " ".join(map(lambda x: ''.join(list(x).__reversed__()), text.split(" ")))


if __name__ == '__main__':
    print("Example:")
    print(backward_string_by_word(''))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    print("Coding complete? Click 'Check' to earn cool rewards!")

# best solutions

# import re
# backward_string_by_word = lambda text: re.sub("\w+", lambda c: c.group(0)[-1::-1], text)
# print(backward_string_by_word("world"))

# return re.sub('\w+',lambda x:x.group()[::-1],s)