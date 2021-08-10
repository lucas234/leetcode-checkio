# coding=utf-8
# auther：Liul5
# date：2019/5/9 13:42
# tools：PyCharm
# Python：2.7.15
# https://py.checkio.org/en/mission/army-battles/


class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5

    def defend(self, opponent):
        self.health -= opponent.attack

    @property
    def is_alive(self):
        return self.health > 0


class Knight(Warrior):
    def __init__(self):
        Warrior.__init__(self)
        self.attack = 7


def fight(unit_1, unit_2):
    a, d = unit_1, unit_2
    while a.is_alive:
        d.defend(a)
        a, d = d, a
    return unit_1.is_alive


class Army(object):
    def add_units(self, obj, num):
        pass


class Battle(object):
    def fight(self, my_army, enemy_army):
        return


# chuck = Warrior()
# bruce = Warrior()
# carl = Knight()
# dave = Warrior()
# mark = Warrior()
#
# print fight(chuck, bruce) == True
# print fight(dave, carl) == False
# print chuck.is_alive == True
# print bruce.is_alive == False
# print carl.is_alive == True
# print dave.is_alive == False
# print fight(carl, mark) == False
# print carl.is_alive == False



chuck = Warrior()
bruce = Warrior()
carl = Knight()
dave = Warrior()

print fight(chuck, bruce) #== True
print fight(dave, carl) #== False
print chuck.is_alive #== True
print bruce.is_alive  # == False
print carl.is_alive #== True
print dave.is_alive #== False