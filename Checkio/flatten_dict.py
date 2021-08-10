# coding=utf-8
# auther：Liul5
# date：2019/5/8 15:08
# tools：PyCharm
# Python：2.7.15
# https://py.checkio.org/en/mission/flatten-dict/


def flatten(init, lkey=''):
    ret = {}
    for rkey, val in init.items():
        key = lkey+rkey
        if not val:
            ret[key] = ""
        if isinstance(val, dict):
            ret.update(flatten(val, key+'/'))
        else:
            ret[key] = val
    return ret


print flatten({"key": "value"}) #== {"key": "value"}
print flatten({"key": {"deeper": {"more": {"enough": "value"}}}})# == {"key/deeper/more/enough": "value"}
print flatten({"empty": {}}) #== {"empty": ""}





