# coding=utf-8
# auther：Liul5
# date：2019/5/5 9:23
# tools：PyCharm
# Python：2.7.15
# https://py.checkio.org/en/mission/every-person-is-unique/
from datetime import datetime


class Person(object):
    def __init__(self, first_name, last_name, birth_date, job, working_years, salary, country, city, gender='unknown'):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.job = job
        self.working_years = working_years
        self.salary = salary
        self.country = country
        self.city = city
        self.gender = gender

    def name(self):
        return self.first_name+" "+self.last_name

    def age(self):
        return (datetime.strptime("01.01.2018", '%d.%m.%Y').date() - datetime.strptime(self.birth_date, '%d.%m.%Y').date()).days/365

    def work(self):
        schema = {"male": "He is a ", "female": "She is a ", "unknown": "Is a "}
        return schema.get(self.gender) + self.job

    def money(self):
        return "%s" % format(12*self.salary*self.working_years, ",").replace(",", " ")

    def home(self):
        return "Lives in " + self.city + ", " + self.country

