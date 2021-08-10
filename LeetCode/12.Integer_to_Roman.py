# @Time    : 2020/10/27 13:38
# @Author  : lucas
# @File    : 12.Integer_to_Roman.py
# @Project : locust demo
# @Software: PyCharm

def int_to_roman(num: int) -> str:
    mapping = {'1': 'I', '5': 'V', '6': 'VI', '7': 'VII', '8': 'VIII', '10': 'X', '50': 'L', '100': 'C', '500': 'D',
               '1000': 'M', '900': 'CM', '90': 'XC',
               '4': 'IV', '9': 'IX', '400': 'CD', '40': 'XL'}
    thousands, _ = divmod(num, 1000)
    percentile, _ = divmod(_, 100)
    tenths, unit = divmod(_, 10)
    return (mapping.get(str(thousands * 1000), "") or thousands * mapping['1000']) + \
           (mapping.get(str(percentile * 100), "") or (
               percentile * mapping['100'] if percentile <= 5 else "D" + (percentile - 5) * mapping['100'])) + \
           (mapping.get(str(tenths * 10), "") or (
               tenths * mapping['10'] if tenths <= 5 else "L" + (tenths - 5) * mapping['10'])) + \
           (mapping.get(str(unit), "") or unit * mapping['1'])


# print(int_to_roman(3))
# print(int_to_roman(4))
# print(int_to_roman(9))
# print(int_to_roman(58))
# print(int_to_roman(1994))

num = 60
RomanNumbers = (1000,900,500,400,100,90,50,40,10,9,5,4,1)
RomanToInt = ("M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I")
RomanNum = ""
while num != 0:
    for i, integer in enumerate(RomanNumbers):
        if num >= integer:
            num -= integer
            RomanNum += RomanToInt[i]
            break
print(RomanNum)
