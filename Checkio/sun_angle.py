# coding=utf-8
# auther：Liul5
# date：2019/3/21 13:14
# tools：PyCharm
# Python：2.7.15
# from __future__ import division
# 日照角（Sun Angle）
# 1.太阳6:00 AM升起，对应0度；12点时正午，对应90度；18:00 PM日落对应180度
# 2.其他时间（早上6点之前和晚上6点之后）返回："I don't see the sun!"
# 3.正常返回对应的角度
# 输入: 时间.
# 输出: 太阳的角度，四舍五入小数点后两位.
# 例子:
# sun_angle("07:00") == 15
# sun_angle("12:15"] == 93.75
# sun_angle("01:23") == "I don't see the sun!"


def sun_angle(_time):
    if int(_time[0:2]) < 6 or int(_time[0:2]) > 18 or int(_time[0:2]) == 18 and int(_time[-2:]) > 0:
        return "I don't see the sun!"
    else:
        all_minutes = (int(_time[0:2]) - 6) * 60 + int(_time[-2:])
        rate = 180.0 / 720
        return all_minutes * rate


print sun_angle("07:00") == 15
print sun_angle("12:15") == 93.75
print sun_angle("01:23") == "I don't see the sun!"
print 180.0/720
print 180.0//720
print 180/720
print 180//720
print 180 % 150


# def sun_angle(time):
#     h, m = list(map(int, time.split(':')))
#     angle = 15 * h + m / 4 - 90
#     return angle if 0 <= angle <= 180 else "I don't see the sun!"





