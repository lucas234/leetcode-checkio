# @Time    : 2020/9/10 16:28
# @Author  : lucas
# @File    : 6.Zig_Zag_Conversion.py
# @Project : locust demo
# @Software: PyCharm

s = "AB"
num_rows = 2
x, y = 0 , 0
result = []
s_list = list(s)
while s_list:
    for _ in range(num_rows):
        if not s_list:
            break
        if (x, y) not in result:
            temp = s_list.pop(0)
            result.append((x, y))
        if y == num_rows-1:
            break
        y += 1

    for _ in range(num_rows-1):
        if not s_list:
            break
        x += 1
        y -= 1
        if (x, y) not in result:
            temp = s_list.pop(0)
            result.append(((x, y)))


print(result)

t = sorted(zip(result,s), key=lambda x:(x[0][1], x[0][0]))
sss = ""
for i in t:
    sss += i[1]
print(sss)


def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s

    row_arr = [""] * numRows
    row_idx = 1
    going_up = True

    for ch in s:
        row_arr[row_idx - 1] += ch
        if row_idx == numRows:
            going_up = False
        elif row_idx == 1:
            going_up = True

        if going_up:
            row_idx += 1
        else:
            row_idx -= 1

    return "".join(row_arr)


print(convert("PAYPALISHIRING", 3))