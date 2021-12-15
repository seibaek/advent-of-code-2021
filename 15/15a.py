aoc_input = open("testinput15", "r")
new_list = aoc_input.read().splitlines()
aoc_input.close()

print(new_list)

print(len(new_list[0]))
print(len(new_list))

total = 0
for v in new_list:
    for w in v:
        total += int(w)
print(total)

# minimum possible score is 198
# maximum possible score is 60893
# construct a list of paths with minimum length
# tree = {}

lowest_risk = 60893

class PathNode:
    def __init__(self, risk, right=None, down=None):
        self.right = right
        self.down = down
        self.risk = risk
    # def print(self):
    #     print(self.risk)

def rec_risk(path, total_risk):
    if path is None:
        return
    new_total = total_risk + path.risk
    if path.right is None and path.down is None:
        global lowest_risk
        if new_total < lowest_risk:
            lowest_risk = new_total
    else:
        rec_risk(path.right, new_total)
        rec_risk(path.down, new_total)



def build_tree(x,y):
    _right = None
    _down = None
    try:
        _right = int(new_list[y][x + 1])
    except:
        pass
    try:
        _down = int(new_list[y+1][x])
    except:
        pass
    return PathNode(int(new_list[y][x]),right=build_tree(_right),down=build_tree(_down))


tree = build_tree(0,0)

print(tree)

# for y in range(len(new_list)):
#     for x in range(len(new_list[0])):



#
#
# for y in range(len(new_list)):
#     for x in range(len(new_list[0])):
#         tree[str(x) + "," + str(y)] = PathNode(new_list[y][x])
#
# for y in range(len(new_list)):
#     for x in range(len(new_list[0])):
#         if str(x + 1) + "," + str(y) in tree.keys():
#             tree[str(x) + "," + str(y)].right = tree[str(x + 1) + "," + str(y)]
#         if str(x) + "," + str(y + 1) in tree.keys():
#             tree[str(x) + "," + str(y)].down = tree[str(x) + "," + str(y + 1)]

        # if y == len(new_list) and x == len(new_list[0]):
        #     pass
        # elif y == len(new_list):
        #     tree[str(x) + "," + str(y)] = PathNode(new_list[y][x])
        #     tree[new_list[y][x]].append([x + 1, y])
        #     tree[new_list[y][x]].append([x, y + 1])
        # elif x == len(new_list[0]):
        #     tree[str(x) + "," + str(y)] = PathNode(new_list[y][x])
        #     tree[new_list[y][x]].append([x + 1, y])
        #     tree[new_list[y][x]].append([x, y + 1])
        # else:
        #     tree[str(x) + "," + str(y)] = PathNode(new_list[y][x])
        #     tree[new_list[y][x]].append([x + 1, y])
        #     tree[new_list[y][x]].append([x, y + 1])

# print(tree('8,8').print())



# root = PathNode(1)
#
# root.print()