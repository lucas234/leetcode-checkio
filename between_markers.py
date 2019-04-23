# coding=utf-8
# auther：Liul5
# date：2019/4/8 14:45
# tools：PyCharm
# Python：2.7.15
# https://py.checkio.org/en/mission/between-markers-simplified/share/0d860a5ed50ee2206c3f89d400ab7eda/


def between_markers(strings, left_marks, right_marks):
    import re
    if left_marks in ['[', '.', '*', ']']:
        left_marks = "\\" + left_marks
    if right_marks in ['[', '.', '*', ']']:
        right_marks = "\\" + right_marks
    pattern = re.compile(r'{0}(.*?){1}'.format(left_marks, right_marks))
    return re.findall(pattern, strings)[0]


print between_markers("What is [apple]", "[", "]") == 'apple'
print between_markers('What is >apple<', '>', '<') == 'apple'


# def between_markers(text: str, begin: str, end: str) -> str:
#     return text.split(sep=end, maxsplit=1)[0].split(sep=begin)[1]
#     '''return text[text.index(begin) + 1 : text.index(end)]'''

# between_markers = lambda text, begin, end: text.split(begin)[1].split(end)[0]
