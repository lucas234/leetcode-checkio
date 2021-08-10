# auther：Liul8
# date：2020/3/31 17:23
# tools：PyCharm
# Python：3.7.7
# https://py.checkio.org/en/mission/first-word/


def first_word(text: str) -> str:
    new_items = text.replace(".", " ").replace(",", " ").strip().split(" ")
    return new_items[0]


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")



# best solutions


# def first_word(text: str) -> str:
#     """
#         returns the first word in a given text.
#     """
#     import re
#
#     return re.findall(r'[\w+\']+', text)[0]