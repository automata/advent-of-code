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

def rec(node, tree, target):
    if node == None or node == []:
        return []
    if isinstance(node, str):
        # print(node)
        if node == target:
            return [True]
        return rec(tree[node], tree, target)
    if isinstance(node, tuple) and len(node) > 1:
        return rec(node[1], tree, target)
    if isinstance(node, list):
        return rec(node[0], tree, target) + rec(node[1:], tree,target)

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
    s = 0
    for bag_type in bag_tree.keys():
        if bag_type != target_bag:
            ret = rec(bag_type, bag_tree, target_bag)
            if sum(ret) > 0:
                print(bag_type)
                s += 1
    print(s)
