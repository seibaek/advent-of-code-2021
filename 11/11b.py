aoc_input = open("input11.txt", "r")
new_list = aoc_input.read().splitlines()
aoc_input.close()

flash_count = 0
# increase all by one

def splitter(row):
    return [int(x) for x in row]

dumbo_grid = []

for line in new_list:
    dumbo_grid.append(splitter(line))

step_limit = 100
step_count = 0

def steps(in_list):
    out_list = in_list.copy()
    for i, v in enumerate(in_list):
        for ji, jv in enumerate(v):
            out_list[i][ji] = jv + 1
    out_list = flash(out_list)
    return out_list

def flash(in_list):
    out_list = in_list.copy()
    exploding = False
    global flash_count
    for x, xv in enumerate(in_list):
        for y, yv in enumerate(xv):
            if in_list[x][y] > 9:
                try:
                    if out_list[x + 1][y] != 0:
                        out_list[x + 1][y] += 1 # east
                        if out_list[x + 1][y] > 9:
                            exploding = True
                except IndexError:
                    pass
                try:
                    if x - 1 > -1:
                        if out_list[x - 1][y] != 0:
                            out_list[x - 1][y] += 1 # west
                            if out_list[x - 1][y] > 9:
                                exploding = True
                except IndexError:
                    pass
                try:
                    if out_list[x][y + 1] != 0:
                        out_list[x][y + 1] += 1 # north
                        if out_list[x][y + 1] > 9:
                            exploding = True
                except IndexError:
                    pass
                try:
                    if y - 1 > -1:
                        if out_list[x][y - 1] != 0:
                            out_list[x][y - 1] += 1 # south
                            if out_list[x][y - 1] > 9:
                                exploding = True
                except IndexError:
                    pass
                try:
                    if out_list[x + 1][y + 1] != 0:
                        out_list[x + 1][y + 1] += 1 # north east
                        if out_list[x + 1][y + 1] > 9:
                            exploding = True
                except IndexError:
                    pass
                try:
                    if y - 1 > -1:
                        if out_list[x + 1][y - 1] != 0:
                            out_list[x + 1][y - 1] += 1 # south east
                            if out_list[x + 1][y - 1] > 9:
                                exploding = True
                except IndexError:
                    pass
                try:
                    if x - 1 > -1:
                        if out_list[x - 1][y + 1] != 0:
                            out_list[x - 1][y + 1] += 1 # north west
                            if out_list[x - 1][y + 1] > 9:
                                exploding = True
                except IndexError:
                    pass
                try:
                    if x - 1 > -1 and y - 1 > -1:
                        if out_list[x - 1][y - 1] != 0:
                            out_list[x - 1][y - 1] += 1 # north east
                            if out_list[x - 1][y - 1] > 9:
                                exploding = True
                except IndexError:
                    pass
                out_list[x][y] = 0
                flash_count += 1
    if exploding == False:
        return out_list
    else:
        return flash(out_list)

def flash_checker(in_list):
    synchro = True
    for i, v in enumerate(in_list):
        for ji, jv in enumerate(v):
            if jv != 0:
                synchro = False
    return synchro

step_index = 0

while flash_checker(dumbo_grid) == False:
    dumbo_grid = steps(dumbo_grid)
    step_index += 1
    if flash_checker(dumbo_grid):
        print(step_index)