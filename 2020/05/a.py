def dec(c):
    cl = list(c)
    rows = cl[:7]
    cols = cl[-3:]
    print(rows, cols)
    low = 0
    up = 127
    #print(low, up)
    for r in rows:
        d = abs(up - low)
        if r == "F":
            up = low + d // 2
        else:
            low = low + d // 2 + 1
        #print(low, up)

    l = 0
    rr = 7
    for c in cols:
        d = abs(l - rr)
        if c == "L":
            rr = l + d // 2
        else:
            l = l + d // 2 + 1
        #print(l, rr)


    return low, l

with open("input.txt") as f:
    l = f.read().splitlines()
    max_seat_id = 0
    for ll in l:
        r,c = dec(ll)
        seat_id = r * 8 + c
        if seat_id > max_seat_id:
            max_seat_id = seat_id
        print(seat_id)
    print(max_seat_id)


# 0                     127 
# 0           63              F
#      32     63 
#      32  47
