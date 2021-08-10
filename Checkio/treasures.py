# coding=utf-8
# auther：Liul5
# date：2019/5/16 15:16
# tools：PyCharm
# Python：2.7.15
# https://py.checkio.org/en/mission/treasures/


def treasures(info, limit):
    # input sorting varies in the result check, so I had to introduce a sorted list
    info_sort = ['golden coin', 'silver coin', 'ruby']
    rank = sorted(info, key=lambda x: info[x]["price"] / info[x]["weight"], reverse=True)
    limit = limit*1000
    for treas in rank:
        quant = int(min(info[treas]['amount'], limit // info[treas]['weight']))
        limit -= quant * info[treas]['weight']
        info[treas]['take'] = quant

    return [treas + ': ' + str(info[treas]['take']) for treas in info_sort if info[treas]['take'] > 0]


print treasures({'golden coin':
              {'price': 100, 'weight': 50, 'amount': 200},
           'silver coin':
              {'price': 10, 'weight': 20, 'amount': 1000},
           'ruby':
              {'price': 1000, 'weight': 200, 'amount': 2}}, 5) == [
               'golden coin: 92', 'ruby: 2']

# from scipy.optimize import linprog
#
#
# def treasures(info, limit):
#     treasures = ('golden coin', 'silver coin', 'ruby')
#
#     prices = [-info[i]['price'] for i in treasures ]
#     weights = [[info[i]['weight'] for i in treasures ]]
#     total_weight = [1000 * limit]
#     bounds = [(0, info[i]['amount']) for i in treasures ]
#
#     r = linprog(prices, weights, total_weight, bounds=bounds)
#
#     return [f'{i}: {int(a)}' for i, a in zip(treasures , r.x) if a > 0]

info = {'golden coin':
              {'price': 100, 'weight': 50, 'amount': 200},
           'silver coin':
              {'price': 10, 'weight': 20, 'amount': 1000},
           'ruby':
              {'price': 1000, 'weight': 200, 'amount': 2}}

print sorted(info, key=lambda x: info[x]["price"] / info[x]["weight"], reverse=True)
print sorted(info.items(), key=lambda x: x[1]["price"] / x[1]["weight"], reverse=True)
print info.keys()
