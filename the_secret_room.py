# coding=utf-8
# auther：Liul5
# date：2019/4/28 14:02
# tools：PyCharm
# Python：2.7.15
# https://py.checkio.org/en/mission/the-secret-room/


def change(n):
    book = {0: '',
            1: 'one', 11: 'eleven', 10: 'ten',
            2: 'two', 12: 'twelve', 20: 'twenty',
            3: 'three', 13: 'thirteen', 30: 'thirty',
            4: 'four', 14: 'fourteen', 40: 'forty',
            5: 'five', 15: 'fifteen', 50: 'fifty',
            6: 'six', 16: 'sixteen', 60: 'sixty',
            7: 'seven', 17: 'seventeen', 70: 'seventy',
            8: 'eight', 18: 'eighteen', 80: 'eighty',
            9: 'nine', 19: 'nineteen', 90: 'ninety'
            }
    if n == 1000: return 'one thousand'
    hundreds = book[n // 100] + ' hundred' * bool(book[n // 100])
    tens = book[n % 100] if book.get(n % 100) else book[(n % 100) // 10 * 10]
    units = '' if book.get(n % 100) else book[n % 10]
    return ' '.join((hundreds, tens, units)).strip()


secret_room = lambda number: sorted(change(key) for key in range(1, number + 1)).index(change(number)) + 1


#
# BELOW_20 = [None, 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
#             'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
#             'sixteen', 'seventeen', 'eighteen', 'nineteen']
# TENS = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
#
# def word(nb):
#     """Write numbers 1 to 1000 in words (and 0 --> '')."""
#     if 0 <= nb < 20:
#         res = [BELOW_20[nb]]
#     elif 20 <= nb < 100:
#         tens, below_ten = divmod(nb, 10)
#         res = [TENS[tens - 2], BELOW_20[below_ten]]
#     elif 100 <= nb < 1000:
#         hundreds, below_hundred = divmod(nb, 100)
#         res = [BELOW_20[hundreds], 'hundred', word(below_hundred)]
#     else:
#         res = ['one', 'thousand']
#     return ' '.join(elem for elem in res if elem) # remove possible None / 0.
#
# secret_room = lambda door: sum(word(nb) < word(door) for nb in range(door))
