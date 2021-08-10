# coding=utf-8
# 时间转换(24h转换为12h)
# https://py.checkio.org/en/mission/time-converter-24h-to-12h/
# 1.中午之前输出格式：'hh:mm a.m.'，中午之后输出格式：'hh:mm p.m.'
# 2.如果小时小于10，则不要写前边的0，例如：'9:05 a.m.'
# 3.图中看出'00:00'时，应显示：'12:00 a.m.'
# 输入: 24小时的时间格式字符串.
# 输出: 12小时的时间格式字符串.
# 例子:
# time_converter('12:30') == '12:30 p.m.'
# time_converter('09:00') == '9:00 a.m.'
# time_converter('23:15') == '11:15 p.m.'


def time_converter(time_str):
    hours = time_str.split(":")[0]
    minute = time_str.split(":")[1]
    if int(hours) > 12:
        _time = str(int(hours) - 12) + ":" + minute + " p.m."
    elif int(hours) == 12:
        _time = time_str + " p.m."
    elif int(hours) == 0 and int(minute) == 0:
        _time = str(12 - int(hours)) + ":" + minute + " a.m."
    else:
        _time = str(int(hours)) + ":" + minute + " a.m."
    return _time


print time_converter('12:30') == '12:30 p.m.'
print time_converter('09:00') == '9:00 a.m.'
print time_converter('23:15') == '11:15 p.m.'
print time_converter('00:00') == '12:00 a.m.'

# second py3
# from datetime import datetime
#
#
# def time_converter1(time):
#     return (datetime.strptime(time, "%H:%M").strftime("%I:%M %p").replace('PM', 'p.m.').replace('AM', 'a.m.').lstrip('0'))
#
# # third py3
# import time
#
# def time_converter2(t):
#     t = time.strptime(t, '%H:%M')
#     t = time.strftime('%l:%M {%p}', t).lstrip()
#     return t.format(AM='a.m.', PM='p.m.')
#
# print time_converter2("09:30")

