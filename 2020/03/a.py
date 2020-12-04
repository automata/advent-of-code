with open("input0.txt") as f:
    l = f.readlines()
    trees = 0
    pos = 0
    for ll in l[1:]:
        ll = ll[:-1]
        pos = pos + 3
        if pos > len(ll):
            ll = ll + (ll * pos)
        print(pos, ll, len(ll))
        if ll[pos] == "#":
            trees += 1
    print(trees)
