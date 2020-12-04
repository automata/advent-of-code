def ok(pas, let, mi, ma):
    count = 0
    for c in pas:
        if c == let:
            count +=1
    return (count >= mi) and (count <= ma)

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

