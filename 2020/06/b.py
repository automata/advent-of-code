import string

def intersec(lists, lp): 
    s = lists[0]
    for i in range(1, len(lists)):
        if len(lists[i]) > 0:
            s = set(s) & set(lists[i])
    ss = list(s)
    return ss

with open("input.txt") as f:
    ga = f.read().split('\n\n')
    qs = 0
    for g in ga:
        p = g.split('\n')
        pl = [list(x) for x in p]
        pi = intersec(pl, len(p))
        qr = len(pi)
        qs += qr
        print(pl, pi, qr)
    print(qs)
