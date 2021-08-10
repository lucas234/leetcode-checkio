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


# https://py.checkio.org/en/mission/between-markers/

# def between_markers(text: str, begin: str, end: str) -> str:
#     """
#         returns substring between two given markers
#     """
#     # your code here
#     if begin in text and end in text:
#         if text.index(begin) < text.index(end):
#             return text.split(begin)[1].split(end)[0]
#         else:
#             return ""
#     elif begin in text and end not in text:
#         return text.split(begin)[1]
#     elif begin not in text and end in text:
#         return "No"
#     else:
#         return text
#
#
# if __name__ == '__main__':
#     print('Example:')
#     print(between_markers('What is >apple<', '>', '<'))
#
#     # These "asserts" are used for self-checking and not for testing
#     assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
#     assert between_markers("<head><title>My new site</title></head>",
#                            "<title>", "</title>") == "My new site", "HTML"
#     assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
#     assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
#     assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
#     assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
#     print('Wow, you are doing pretty good. Time to check it!')
