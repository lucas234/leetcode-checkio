# coding=utf-8
# auther：Liul5
# date：2019/3/25 10:42
# tools：PyCharm
# Python：2.7.15


class Warrior(object):
    def __init__(self):
        self.health = 50
        self.attack = 5
        self.is_alive = self.health > 0


class Knight(Warrior):
    def __init__(self):
        Warrior.__init__(self)  # 继承父类的构造方法，也可以写成：super(Warrior,self).__init__()
        self.attack = 7


def fight(first_warrior, second_warrior):
    while True:
        second_warrior.health -= first_warrior.attack
        first_warrior.health -= second_warrior.attack
        # print first_warrior.health, second_warrior.health
        if first_warrior.health < 0:
            first_warrior.is_alive = False
        if second_warrior.health < 0:
            second_warrior.is_alive = False
        if first_warrior.health > 0 >= second_warrior.health:
            return True
        if first_warrior.health < 0 < second_warrior.health:
            return False
        if first_warrior.health <= 0 and second_warrior.health <= 0:
            first_warrior.is_alive = True
            second_warrior.is_alive = False
            return True


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

# """Just two more attack points!
# """
#
#
# class Warrior:
#     health = 50
#     attack = 5
#
#     @property
#     def is_alive(self):
#         return self.health > 0
#
#
# class Knight(Warrior):
#     attack = 7
#
#
# def fight(a, b):
#     while a.is_alive and b.is_alive:
#         b.health -= a.attack
#         if b.is_alive:
#             a.health -= b.attack
#     return a.is_alive


# class Warrior:
#     def __init__(self):
#         self.health = 50
#         self.attack = 5
#
#     def defend(self, opponent):
#         self.health -= opponent.attack
#
#     @property
#     def is_alive(self):
#         return self.health > 0
#
#
# class Knight(Warrior):
#     def __init__(self):
#         super().__init__()
#         self.attack = 7
#
#
# def fight(unit_1, unit_2):
#     a, d = unit_1, unit_2
#     while a.is_alive:
#         d.defend(a)
#         a, d = d, a
#
#     return unit_1.is_alive