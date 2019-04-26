# coding=utf-8
# auther：Liul5
# date：2019/4/26 14:10
# tools：PyCharm
# Python：2.7.15
# https://py.checkio.org/en/mission/date-and-time-converter/
months = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June",
          "07": "July", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}


def date_time(time_str):
    day, month, year = time_str.split(" ")[0].split(".")
    hour, minute = time_str.split(" ")[1].split(":")
    hour = (str(int(hour)) + " hour") if hour == "01" else (str(int(hour)) + " hours")
    minute = (str(int(minute)) + " minute") if minute == "01" else (str(int(minute)) + " minutes")
    return "{0} {1} {2} year {3} {4}".format(int(day), months.get(month), year, hour, minute)


print date_time("01.01.2000 00:00") #== "1 January 2000 year 0 hours 0 minutes"
print date_time("19.09.2999 01:59") #== "19 September 2999 year 1 hour 59 minutes"
print date_time("21.10.1999 18:01") #== "21 October 1999 year 18 hours 1 minute"


# from datetime import datetime
#
#
# def date_time(time: str) -> str:
#     dt = datetime.strptime(time, '%d.%m.%Y %H:%M')
#     day = dt.day
#     hour = dt.hour
#     minute = dt.minute
#     dt = dt.strftime(f"{day} %B %Y year "
#                      f"{hour} {'hours' if hour != 1 else 'hour'} "
#                      f"{minute} {'minutes' if minute != 1 else 'minute'}")
#     return dt