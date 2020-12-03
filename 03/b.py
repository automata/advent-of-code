slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]

def has_tree(pos, slope, ln):
    r, d = slope
    pos = pos + r
    if pos >= len(ln):
        missing = pos - len(ln) + 1
        ln = ln + (ln * missing)
    return ln[pos] == "#", pos


with open("input.txt") as f:
    l = f.readlines()
    prod = 1
    for slope in slopes:
        pos = 0
        trees = 0
        r, d = slope
        for idx in range(0, len(l)-d, d):
            ll = l[idx][:-1]
            ln = l[idx+d][:-1]
            hasit, pos = has_tree(pos, slope, ln)
            if hasit:
                trees += 1
        print(slope, trees)
        if trees > 0:
            prod *= trees

    print(prod, trees)
