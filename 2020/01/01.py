with open("./input.txt", "r") as f:
    l = f.readlines()
    for li in l:
        for lj in l:
            for lk in l:
                ni = int(li)
                nj = int(lj)
                nk = int(lk)
                if (ni != nj) and (nj != nk):
                    s = ni + nj + nk
                    if s == 2020:
                        print(ni, nj, nk, s, ni * nj * nk)
