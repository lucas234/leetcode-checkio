# coding=utf-8
# auther：Liul5
# date：2019/3/29 13:41
# tools：PyCharm
# Python：2.7.15


def house(plan):
    if "#" not in plan:
        return 0
    plan = plan.split()
    # print plan
    raw = [i for i, j in enumerate(plan) for m, n in enumerate(j) if n == "#"]
    column = [m for i, j in enumerate(plan) for m, n in enumerate(j) if n == "#"]
    raw_max = max(raw)
    raw_min = min(raw)
    column_max = max(column)
    column_min = min(column)
    # print [(i,m) for i, j in enumerate(plan) for m, n in enumerate(j) if n == "#"]
    return (raw_max - raw_min + 1) * (column_max - column_min + 1)


print house('''
0000000
##00##0
######0
##00##0
#0000#0
''')  # 24
print house("\n0000000000\n000###0000\n000#######\n000###0000\n")  # 21
