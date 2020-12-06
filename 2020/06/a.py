import string

with open("input.txt") as f:
    ga = f.read().split('\n\n')
    qs = 0
    for g in ga:
        p = g.split('\n')
        pj = "".join(p)
        pl = list(pj)
        ps = set(pl)
        qr = len(ps)
        qs += qr
        print(ps, qr)
    print(qs)
