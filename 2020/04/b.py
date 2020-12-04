from pprint import pprint

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.

def is_valid_value(d):
    id,val = d
    if id == "byr":
        if len(val) == 4:
            vali = int(val)
            return vali >= 1920 and vali <= 2002
    if id == "iyr":
        if len(val) == 4:
            vali = int(val)
            return vali >= 2010 and vali <= 2020
    if id == "eyr":
        if len(val) == 4:
            vali = int(val)
            return vali >= 2020 and vali <= 2030
    if id == "hgt":
        suf = val[-2:]
        if suf == "cm":
            vali = int(val[:-2])
            return vali >= 150 and vali <= 193
        if suf == "in":
            vali = int(val[:-2])
            return vali >= 59 and vali <= 76
    if id == "hcl":
        if val[0] == "#":
            c = val[1:]
            if len(c) == 6:
                for ci in c:
                    is_num = ci in [str(x) for x in range(10)]
                    is_let = ci in "a b c d e f".split(" ")
                    return is_num or is_let
    if id == "ecl":
        if len(val) == 3:
            return val in "amb blu brn gry grn hzl oth".split(" ")
    if id == "pid":
        return len(val) == 9
    if id == "cid":
       return True
    return False


def is_valid(doc):
    req = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"] # cid
    c = 0
    for d in doc:
        if (d[0] in req) and is_valid_value(d):
            c += 1
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
