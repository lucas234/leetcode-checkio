# coding=utf-8
# auther：Liul5
# date：2019/4/22 17:44
# tools：PyCharm
# Python：2.7.15
# https://py.checkio.org/en/mission/speechmodule/
schema = {0: 'zero', 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six",
          7: "seven", 8: "eight", 9: "nine", 10: 'ten', 11: 'eleven', 12: 'twelve',
          13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
          18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty',
          50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}


def checkio(number):
    hundred, mod = divmod(number, 100)
    ten, unit = divmod(mod, 10)
    if number <= 20 or number in [30, 40, 50, 60, 70, 80, 90]:
        return schema.get(number)
    if hundred != 0:
        if ten == 0 and unit == 0:
            return schema.get(hundred) + " hundred"
        if ten == 0:
            return schema.get(hundred) + " hundred " + schema.get(unit)
        if ten == 1:
            return schema.get(hundred) + " hundred " + schema.get(ten * 10 + unit)
        if ten > 1 and unit == 0:
            return schema.get(hundred) + " hundred " + schema.get(ten * 10)
        else:
            return schema.get(hundred) + " hundred " + schema.get(ten * 10) + " " + schema.get(unit)
    if hundred == 0 and ten != 0:
        return schema.get(ten*10) + " " + schema.get(unit)


print checkio(1) #== 'four'
print checkio(143) #== 'one hundred forty three'
print checkio(12) #== 'twelve'
print checkio(101) #== 'one hundred one'
print checkio(212) #== 'two hundred twelve'
print checkio(40) #== 'forty'
print checkio(40) #== 'forty'
assert checkio(40) #== 'forty'

