
seats = []

with open('input/input5.txt') as f:
    for line in f:
        seats.append(line.strip())


def row_column(seat):
    low = 0
    high = 127
    for s in seat[:7]:
        if s == 'F':
            high = (high+low)//2
        elif s == 'B':
            low = (high+low+1)//2


    assert low == high
    row = low

    low = 0
    high = 7
    for s in seat[-3:]:
        if s == 'L':
            high = (high+low)//2
        elif s == 'R':
            low = (high+low+1)//2


    assert low == high
    col = low

    return row, col


def seat_id(s):
    v = row_column(s)
    return v[0]*8+v[1]


id_list = []
m = 0
for s in seats:
    sid = seat_id(s)
    id_list.append(sid)
    if sid > m:
        m = sid

print(m)

id_list = sorted(id_list)
start = id_list[0] + 1
while start in id_list:
    start += 1
print(start)
