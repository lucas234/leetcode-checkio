# auther：Liul8
# date：2020/4/20 16:33
# tools：PyCharm
# Python：3.7.7
# https://py.checkio.org/en/mission/three-words/


def checkio(words: str) -> bool:
    count = 0
    for i in words.split():
        if not i.isalpha():
            count = 0
        if i.isdigit():
            count = count - 1
        count += 1
        if count == 3:
            return True
    return False


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))

    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")


# best solutions

# import re
#
# def checkio(words: str) -> bool:
#     match = re.search("([a-zA-Z]+\s){2}[a-zA-Z]+", words)
#     if match:
#         print (match[0])
#         return True
#     return False