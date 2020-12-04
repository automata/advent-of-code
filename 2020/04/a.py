from pprint import pprint

def is_valid(doc):
    req = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"] # cid
    c = 0
    for d in doc:
        if d[0] in req: c += 1
    return c == len(req)


with open("input.txt") as f:
    l = f.read().splitlines()
    doc = []
    v = 0
    for ll in l:
        if ll == "":
            if is_valid(doc):
                v += 1
            pprint(doc)
            doc = []
        else:
            entry = ll.split(" ")
            for e in entry:
                id, val = e.split(":")
                doc.append((id,val))
    print(v)
