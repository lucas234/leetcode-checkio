# coding=utf-8
# auther：Liul5
# date：2019/3/27 9:19
# tools：PyCharm
# Python：2.7.15


class Friends(object):
    def __init__(self, friends):
        connections = []
        [connections.append(i) if i not in connections else "" for i in list(friends)]
        self.friends = connections

    def add(self, connection):
        if connection in self.friends:
            return False
        else:
            self.friends.append(connection)
            return True

    def remove(self, connection):
        if connection in self.friends:
            self.friends.remove(connection)
            return True
        else:
            return False

    def names(self):
        return reduce(lambda x, y: x | y, self.friends)

    def connected(self, name):
        return reduce(lambda x, y: x | y, [connection.difference({name}) if name in connection else set() for connection in self.friends])



_list = ({"a", "b"}, {"b", "c"}, {"c", "a"}, {"b", "a"})

# f = Friends(_list)
# print f.friends
# print f.connected("a")
# print f.names()
# print reduce(lambda x, y: x | y, [{"a", "b"}, {"b", "c"}, {"c", "d"}, {"b", "a"}])


# class Friends(set):
#     def __init__(self, pairs=set()):
#         super().__init__(map(frozenset, pairs))
#
#     def add(self, pair):
#         if pair in self: return False
#         super().add(frozenset(pair))
#         return True
#
#     def remove(self, pair):
#         if pair not in self: return False
#         super().remove(pair)
#         return True
#
#     def names(self):
#         return set().union(*self)
#
#     def connected(self, name):
#         return Friends(filter({name}.issubset, self)).names() - {name}


# class Friends:
#     def __init__(self, connections):
#         self.connections = {frozenset(c)for c in connections}
#
#     def add(self, elem):
#         if elem in self.connections:
#             return False
#         else:
#             self.connections.add(frozenset(elem))
#             return True
#
#     def remove(self, elem):
#         if elem not in self.connections:
#             return False
#         else:
#             self.connections.remove(elem)
#             return True
#
#     def names(self):
#         return set().union(*self.connections)
#
#     def connected(self, elem):
#         return {n for n in self.names()if {n, elem}in self.connections}
#
#
# c = Friends(_list)
# print c.names()
