# auther：Liul8
# date：2020/5/11 10:55
# tools：PyCharm
# Python：3.7.7
# https://py.checkio.org/en/mission/words-order/


def words_order(text: str, words: list) -> bool:
    # your code here
    text = text.split()
    if len(set(words)) != len(words):
        return False
    try:
        words_index = [text.index(i) for i in words]
        if words_index != sorted(words_index):
            return False
    except Exception as e:
        return False
    return True


if __name__ == '__main__':
    print("Example:")
    print(words_order('hi world im here', ['world', 'here']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert words_order('hi world im here', ['world', 'here']) == True
    assert words_order('hi world im here', ['here', 'world']) == False
    assert words_order('hi world im here', ['world']) == True
    assert words_order('hi world im here',
 ['world', 'here', 'hi']) == False
    assert words_order('hi world im here',
 ['world', 'im', 'here']) == True
    assert words_order('hi world im here',
 ['world', 'hi', 'here']) == False
    assert words_order('hi world im here', ['world', 'world']) == False
    assert words_order('hi world im here',
 ['country', 'world']) == False
    assert words_order('hi world im here', ['wo', 'rld']) == False
    assert words_order('', ['world', 'here']) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")


# best solution

# def words_order(text, words):
#     idx = 0
#     text = text.split()
#     for word in words:
#         try:
#             idx = text.index(word, idx) + 1
#         except ValueError:
#             return False
#     return True



# words_order=lambda x,y: [i for i in x.split() if i in y]==y
