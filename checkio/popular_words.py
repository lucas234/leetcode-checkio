# auther：Liul8
# date：2020/4/8 15:13
# tools：PyCharm
# Python：3.7.7
# https://py.checkio.org/en/mission/popular-words/


def popular_words(text: str, words: list) -> dict:
    # your code here
    from collections import Counter
    count_words = Counter(text.replace("\n", " ").split(" "))
    init_words = {x: 0 for x in words}
    for i, j in count_words.items():
        if i.lower() in words:
            init_words[i.lower()] = j
    return init_words


if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")


# best solution

# def popular_words(text: str, words: list) -> dict:
#     words_in_text = tuple(map(str.lower,text.split()))
#     return {word:words_in_text.count(word) for word in words}