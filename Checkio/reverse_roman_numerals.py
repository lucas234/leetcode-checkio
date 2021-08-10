# coding=utf-8
# auther：Liul5
# date：2019/5/9 11:00
# tools：PyCharm
# Python：2.7.15
# https://py.checkio.org/en/mission/reverse-roman-numerals/


def reverse_roman(roman_string):
    map_table = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    if len(roman_string) == 1:
        return map_table.get(roman_string)
    for i in range(1, len(roman_string)):
        x, y = map_table.get(roman_string[i - 1]), map_table.get(roman_string[i])
        if x >= y:
            result += x
        else:
            result -= x
    else:
        result += y
    return result


print reverse_roman('VI') == 6
print reverse_roman('LXXVI') == 76
print reverse_roman('CDXCIX') == 499
print reverse_roman('MMMDCCCLXXXVIII') == 3888


# def reverse_roman(x):
#     z = zip([1,5,10,50,100,500,1000,-2,-2,-20,-20,-200,-200],"I V X L C D M IV IX XL XC CD CM".split(' '))
#     result = 0
#     for a,b in z:
#         result += (x.count(b))*a
#     return result
