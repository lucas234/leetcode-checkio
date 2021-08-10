# auther：Liul8
# date：2020/5/7 13:36
# tools：PyCharm
# Python：3.7.7
# https://py.checkio.org/en/mission/sort-by-extension/

from typing import List


def sort_by_ext(files: List[str]) -> List[str]:
    # your code here
    no_extension = []
    for file in files:
        if file.endswith(".") and file.count(".") == 1 or file.startswith(".") and file.count(".") == 1:
            no_extension.append(file)
            files.remove(file)
    return sorted(no_extension) + sorted(files, key=lambda x: (x[x.rfind(".")+1:], x[:x.rfind(".")+1]))


if __name__ == '__main__':
    print("Example:")
    print(sort_by_ext(['1.cad', '1.bat', '1.aa']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sort_by_ext(['1.cad', '1.bat', '1.aa']) == ['1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '2.bat']) == ['1.aa', '1.bat', '2.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']) == ['.bat', '1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '.aa', '.bat']) == ['.aa', '.bat', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.', '1.aa']) == ['1.', '1.aa', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '1.aa.doc']) == ['1.aa', '1.bat', '1.cad', '1.aa.doc']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.aa.doc']) == ['1.aa', '1.bat', '1.cad', '.aa.doc']
    print("Coding complete? Click 'Check' to earn cool rewards!")

# other solution

# from typing import List
#
#
# def parse_filename(filename):
#     """Return a tuple of extension and the filename minus the extension.
#
#     Note: if the filename portion is null, then the filename is the
#     extension.
#     """
#     rindex = filename.rindex('.')
#     extension = filename[rindex+1:]
#     name = filename[:rindex]
#     if not name:
#         name = extension
#         extension = ''
#     return (extension, name)
#
#
# def sort_by_ext(files: List[str]) -> List[str]:
#     """Return list of files sorted by extension, then name."""
#     # If the key is a tuple, then it represents a series of keys
#     # executed in order.
#     return sorted(files, key=lambda n: parse_filename(n))