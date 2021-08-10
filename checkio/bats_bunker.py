# coding=utf-8
# auther：Liul5
# date：2019/5/7 13:14
# tools：PyCharm
# Python：2.7.15
# https://py.checkio.org/en/mission/bats-bunker/
import Queue


def checkio():
    return


# print checkio([
#     "B--",
#     "---",
#     "--A"]) == 2.83
# print checkio([
#     "B-B",
#     "BW-",
#     "-BA"]) == 4
# print checkio([
#     "BWB--B",
#     "-W-WW-",
#     "B-BWAB"]) == 12
# print checkio([
#     "B---B-",
#     "-WWW-B",
#     "-WA--B",
#     "-W-B--",
#     "-WWW-B",
#     "B-BWB-"]) == 9.24


def get_coordinates(bunker_map):
    alpha_bat, bat, wall = [], [], []
    for i, j in enumerate(bunker_map):
        for m, n in enumerate(j):
            if n == "A":
                alpha_bat.append((i, m))
            if n == "B":
                bat.append((i, m))
            if n == "W":
                wall.append((i, m))
    return alpha_bat, bat, wall


def next_coordinate(current_coordinate, size):
    x, y = current_coordinate
    next_coordinates = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    if x + 1 > size:
        next_coordinates.remove((x + 1, y))
    if x - 1 < 0:
        next_coordinates.remove((x - 1, y))
    if y + 1 > size:
        next_coordinates.remove((x, y + 1))
    if y - 1 < 0:
        next_coordinates.remove((x, y - 1))
    return next_coordinates


example1 = [
    "B--",
    "---",
    "--A"]
nodes = {(2, 2): [(1, 2), (2, 1)], (1,2): [(0, 2), (1, 1)],(2,1):[(1, 1), (2, 0)]}
# print next_coordinate((2, 2), 2)
# print next_coordinate((2, 1), 2)
# coordinates = [(1, 2), (2, 1)]
# wall_coordinates = [(1, 2)]
# print [i for i in coordinates if i not in wall_coordinates]


def get_traverse_nodes(alpha_bat):
    nodes = {}
    paths = []
    next_queue = Queue.Queue()
    next_queue.put(alpha_bat)
    while not next_queue.empty():
        coordinate = next_queue.get()
        next_coordinates = next_coordinate(coordinate, 2)
        if not next_coordinates:
            break
        parent_nodes = nodes.keys()
        next_coordinates = [i for i in next_coordinates if i not in parent_nodes]
        if next_coordinates:
            nodes[coordinate] = next_coordinates
            for i in next_coordinates:
                next_queue.put(i)
    return nodes


def convert(t):
    l = []
    for i in t:
        l.append([i])
    return l


def test(alpha_bat):
    nodes = {}
    paths = []
    next_queue = Queue.Queue()
    next_queue.put(alpha_bat)
    a = convert([alpha_bat])
    while not next_queue.empty():
        coordinate = next_queue.get()
        next_coordinates = next_coordinate(coordinate, 2)
        if not next_coordinates:
            break
        parent_nodes = nodes.keys()
        next_coordinates = [i for i in next_coordinates if i not in parent_nodes]
        nodes[coordinate] = next_coordinates
        b = convert(next_coordinates)
        for m in a:
            for n in b:
                if not n:
                    n.extend(m)
        print a
        a = b
        for i in next_coordinates:
            next_queue.put(i)
    # return b

# print test((2, 2))

result = {(1, 2): [(0, 2), (1, 1)], (0, 1): [(0, 0)], (0, 0): [], (2, 1): [(1, 1), (2, 0)], (0, 2): [(0, 1)], (2, 0): [(1, 0)], (2, 2): [(1, 2), (2, 1)], (1, 0): [(0, 0)], (1, 1): [(0, 1), (1, 0)]}
# print result.get((2, 2))
# print filter(lambda x: (0, 1) in x[1], result.items())
# print result.items()
print [i[0] for i in result.items() if (1, 0) in i[1]]
# print get_traverse_nodes((2, 2))
# print get_traverse_nodes((0, 0))

# r = {(0, 1): [(1, 1), (0, 2)], (1, 2): [(2, 2)], (0, 0): [(1, 0), (0, 1)], (2, 1): [(2, 2)], (0, 2): [(1, 2)], (2, 0): [(2, 1)], (1, 0): [(2, 0), (1, 1)], (1, 1): [(2, 1), (1, 2)]}
# print r.keys()

current = Queue.Queue()
current.put((0, 0))
t = {}
while not current.empty():
    r = current.get()
    parents = [i[0] for i in result.items() if r in i[1]]
    for i in parents:
        t[i] = t.get(i, []).append(i)
        current.put(i)

















# 1#############################
# import math
#
# # raytracing on map abusing low input precision and rounding on stochastic positions
# def iseeyou(a, b, map):
#     ishit = lambda x, y: map[int(round(y))][int(round(x))] == 'W';
#
#     dx, dy = (b[0] - a[0]) / 16.0, (b[1] - a[1]) / 16.0
#     ex, ey = dx / 4.0, dy / 4.0
#     x0, y0 = a[0], a[1]
#
#     for i in range(16):
#         x, y = x0 + i * dx, y0 + i * dy
#         sx1, sy1 = x - ex, y - ey
#         sx2, sy2 = x + ex, y - ey
#         sx3, sy3 = x + ex, y + ey
#         sx4, sy4 = x - ex, y + ey
#         if ishit(sx1, sy1) or ishit(sx2, sy2) or ishit(sx3, sy3) or ishit(sx4, sy4):
#             return False
#
#     return True
#
# # simple wave-spreading search
# def checkio(map):
#     bats = [[(x, y), map[y][x], 0.0] for y in range(len(map)) for x in range(len(map[y])) if 'AB'.count(map[y][x])]
#     alpha = [x for x in bats if x[1] == 'A'][0]
#
#     bats[0][2] = 1.0
#
#     while not alpha[2]:
#         for start in [x for x in bats if x[2]]:
#             for end in bats:
#                 dist = start[2] + math.sqrt((start[0][0] - end[0][0]) ** 2 + (start[0][1] - end[0][1]) ** 2)
#                 if (not end[2] or dist < end[2]) and iseeyou(start[0], end[0], map):
#                     end[2] = dist
#     return round(alpha[2] - 1.0, 2)




# 2##########################
# from fractions import Fraction
#
#
# def canPass(x1, x2, y1, y2, bunker):
#     dx = x1 - x2
#     dy = y1 - y2
#
#     if dx == 0:
#         if y1 > y2:
#             y1, y2 = y2, y1
#         for c in bunker[x1][y1:y2 + 1]:
#             if c == 'W':
#                 return False
#         return True
#
#     if dy == 0:
#         if x1 > x2:
#             x1, x2 = x2, x1
#         for c in bunker[x1:x2 + 1]:
#             if c[y1] == 'W':
#                 return False
#         return True
#
#     if abs(dx) >= abs(dy):
#         k = Fraction(dy, dx)
#         if dx > 0:
#             x1, y1, x2, y2 = x2, y2, x1, y1
#         start = y1 + k/2
#         for i in range(abs(dx)):
#             nowy = start + i * k
#             nowx = x1 + i
#             if bunker[nowx][int(nowy+.5)] == 'W' or bunker[nowx+1][int(nowy+.5)] == 'W':
#                 return False
#             if int(nowy+.5) == nowy+.5:
#                 if bunker[nowx][int(nowy+.5)-1] == 'W' or bunker[nowx+1][int(nowy+.5)-1] == 'W':
#                     return False
#         return True
#
#     if abs(dx) < abs(dy):
#         k = Fraction(dx, dy)
#         if dy > 0:
#             x1, y1, x2, y2 = x2, y2, x1, y1
#         start = x1 + k/2
#         for i in range(abs(dy)):
#             nowx = start + i * k
#             nowy = y1 + i
#             if bunker[int(nowx+.5)][nowy] == 'W' or bunker[int(nowx+.5)][nowy+1] == 'W':
#                 return False
#             if int(nowx+.5) == nowx+.5:
#                 if bunker[int(nowx+.5)-1][nowy] == 'W' or bunker[int(nowx+.5)-1][nowy+1] == 'W':
#                     return False
#         return True
#
#     return True
#
#
# def distance(x, y):
#     x1, y1 = x
#     x2, y2 = y
#     return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** .5
#
#
# def checkio(bunker):
#     width = len(bunker)
#     length = len(bunker[0])
#     bats = []
#     dest = (0, 0)
#     neighbor = {}
#     for i in range(width):
#         for j in range(length):
#             if bunker[i][j] == 'B':
#                 bats.append((i, j))
#             if bunker[i][j] == 'A':
#                 bats.append((i, j))
#                 dest = (i, j)
#     batsNum = len(bats)
#     for i in range(batsNum - 1):
#         for j in range(i + 1, batsNum):
#             x1, y1 = bats[i]
#             x2, y2 = bats[j]
#             if canPass(x1, x2, y1, y2, bunker):
#                 neighbor.setdefault(bats[i], []).append(bats[j])
#                 neighbor.setdefault(bats[j], []).append(bats[i])
#     active = (0, 0)
#     open = [active]
#     closed = []
#     status = dict()
#     status[active] = (0, distance(active, dest), None)
#     while active != dest:
#         open.remove(active)
#         closed.append(active)
#         nxt = neighbor[active]
#         for n in nxt:
#             if n in closed:
#                 continue
#             if n not in open:
#                 open.append(n)
#                 status[n] = [status[active][0] + distance(n, active), distance(n, dest), active]
#             else:
#                 disg = status[active][0] + distance(n, active)
#                 if status[n][0] > disg:
#                     status[n][0] = disg
#                     status[n][2] = active
#         f = 10000
#         for i in open:
#             if status[i][0] + status[i][1] < f:
#                 f = status[i][0] + status[i][1]
#                 active = i
#     now = active
#     while status[now][2]:
#         now = status[now][2]
#
#     return status[active][0] + status[active][1]


#3###############################
# import copy


# def checkio(bunker):
#     def distance(k1, k2):
#         [x1, y1] = k1
#         [x2, y2] = k2
#         for i in range(min(x1, x2), max(x1, x2) + 1):
#             for j in range(min(y1, y2), max(y1, y2) + 1):
#                 if bunker[i][j] == "W":
#                     if x1 == x2 or y1 == y2:
#                         return 999
#                     else:
#                         k = ((y2 - y1) / (x2 - x1))
#                         d = abs(k * i - j - k * x1 + y1) / (k ** 2 + 1) ** 0.5
#                         if d <= 2 ** 0.5 / 2:
#                             return 999
#         return ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
#
#     if bunker[0][0] == "A":
#         return 0
#     batlist = []
#     for i in range(len(bunker)):
#         for j in range(len(bunker[0])):
#             if bunker[i][j] == "B":
#                 batlist.append([i, j])
#             if bunker[i][j] == "A":
#                 batlist.append([i, j])
#                 [Arow, Acolumn] = [i, j]
#     batlist = list(enumerate(batlist))
#     for i in batlist:
#         if [Arow, Acolumn] == i[1]:
#             Adot = i[0]
#
#     distancelist = []
#     for i in range(len(batlist)):
#         for j in range(i + 1, len(batlist)):
#             distancelist.append([batlist[i][0], batlist[j][0], distance(batlist[i][1], batlist[j][1])])
#
#     unvisited = [i for i in range(1, len(batlist))]
#     while unvisited:
#         dot = min(unvisited, key=lambda x: distancelist[x - 1][2])
#         unvisited.remove(dot)
#         for i in unvisited:
#             for j in distancelist:
#                 if [dot, i] == [j[0], j[1]] or [dot, i] == [j[1], j[0]]:
#                     extradistance = j[2]
#                     break
#             distancelist[i - 1][2] = min(distancelist[i - 1][2], distancelist[dot - 1][2] + extradistance)
#
#     if distancelist[Adot - 1][2] == 999:
#         return None
#     else:
#         return round(distancelist[Adot - 1][2], 2)