
def has_tree(pos, slope, ll, ln, line_num):
    r, d = slope
    pos = pos + r
    if pos > len(ll):
        missing = pos - len(ll)
        ll = ll + (ll * missing)
        ln = ln + (ln * missing)
    #print(slope,pos, ll, len(ll))
    nl = list(ll)
    if pos >= len(ll):
        # nl[pos] = 'X'
        print(line_num, "".join(nl), "???")
        return False, pos
    if d > 1:
        if ln[pos] == "#":
           nl = list(ln)
           nl[pos] = 'X'
           print(line_num, "".join(nl))
           return True, pos
    if ll[pos] == "#":
        nl[pos] = 'X'
        print(line_num, "".join(nl))
        return True, pos
    nl[pos] = 'O'
    print(line_num, "".join(nl))
    return False, pos

#slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
slopes = [(1,1)]

with open("input.txt") as f:
    l = f.readlines()
    prod = 1
    for slope in slopes:
        pos = 0
        trees = 0
        print("0 {}".format(l[0]))
        for idx,ll in enumerate(l[1:]):
            ll = ll[:-1]
            if idx < (len(l)-3):
                ln = l[idx+3]
            else:
                if slope[1] > 1: continue
            hasit, pos = has_tree(pos, slope, ll, ln, idx+1)
            #print("{} {}\n{}\n{}".format(idx, hasit, ll, ln))
            if hasit:
                trees += 1
        print(slope, trees)
        if trees > 0:
            prod *= trees

    print(prod, trees)
