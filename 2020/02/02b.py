def ok(pas, let, mi, ma):
    mi = mi-1
    ma = ma-1
    return ((pas[mi] == let) or (pas[ma] == let)) and (pas[mi] != pas[ma])

with open("input.txt", "r") as f:
    l = f.readlines()
    count = 0
    for li in l:
        pol, let, pas = li.split(" ")
        let = let[:-1]
        mi, ma = pol.split("-")

        if ok(pas, let, int(mi), int(ma)):
            count += 1
            print(pas)
    print(count)

