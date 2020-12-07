from pprint import pprint

def sing(s):
    if s[-1] == "s":
        return s[:-1]
    return s

def proc(s):
    num, *foo = s.strip().strip(".").split(" ")
    if num == "no":
        return None
    num = int(num)
    foo = " ".join(foo)
    foo = sing(foo)

    return num, foo

def rec(node, tree):
    if node == [None]:
        return 0
    if isinstance(node, str):
        return rec(tree[node], tree)
    if isinstance(node, tuple):
        return node[0]
    if isinstance(node, list):
        c = 0
        for b in node:
            c += b[0] * (rec(b[1], tree) + 1)
        return c

with open("input.txt") as f:
    l = f.read().splitlines()
    bag_tree = {}
    for ll in l:
        contains = [s.strip() for s in ll.split("contain")]
        bag_type = sing(contains[0])
        bag_content = [proc(s) for s in contains[1].split(",")]
        bag_tree[bag_type] = bag_content
    pprint(bag_tree)

    target_bag = "shiny gold bag"
    print(rec(target_bag, bag_tree))
