# coding=utf-8
# auther：Liul5
# date：2019/3/29 11:29
# tools：PyCharm
# Python：2.7.15


def two_teams(sailors):
    teams_list = [[], []]
    [teams_list[1].append(i) if 20 <= j <= 40 else teams_list[0].append(i) for i, j in sailors.items()]
    return map(sorted, teams_list)

print two_teams({
    'Smith': 34,
    'Wesson': 22,
    'Coleman': 45,
    'Abrahams': 19}) == [
        ['Abrahams', 'Coleman'],
        ['Smith', 'Wesson']
    ]

print two_teams({
        'Fernandes': 18,
        'Johnson': 22,
        'Kale': 41,
        'McCortney': 54}) == [
            ['Fernandes', 'Kale', 'McCortney'],
            ['Johnson']
            ]