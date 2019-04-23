# coding=utf-8
# auther：Liul5
# date：2019/3/20 10:59
# tools：PyCharm
# Python：2.7.15

# 鸟语
# https://py.checkio.org/en/mission/bird-language/
# 1.每一个辅音字母后都会随机跟随一个元音字母（l ⇒ la or le）
# 2.每一个元音字母后边都会跟随两个相同的字母(a ⇒ aaa)
# 3.元音字母 letters == "aeiouy"
# 输入: 一段鸟语字符.
# 输出: 翻译成一句话.
# 例子:
# translate("hieeelalaooo") == "hello"
# translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
# translate("aaa bo cy da eee fe") == "a b c d e f"
# translate("sooooso aaaaaaaaa") == "sos aaa"


# vowels_letters = "aeiouy"
# import string
# letters = set(string.ascii_lowercase)-set(vowels_letters)
# print "".join(letters)


def translate(_str):
    import re
    pattern = re.compile(r"[cbdgfhkjmlnqpsrtwvxz][aeiouy]|[aeiouy]{3}")
    return re.sub(pattern, lambda m: m.group(0)[0], _str)


print translate("hieeelalaooo") == "hello"
print translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
print translate("aaa bo cy da eee fe") == "a b c d e f"
print translate("sooooso aaaaaaaaa") == "sos aaa"

import re
print re.sub(r'(\w)\1?.', r'\1', "hoooowe yyyooouuu duoooiiine")

