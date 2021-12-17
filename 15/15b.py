aoc_input = open("input15.txt", "r")
new_list = aoc_input.read().splitlines()
aoc_input.close()

big_list = new_list.copy()

for i in range(4 * len(new_list)):
    big_list.append("")

for m in range(1, 5):
    for i, row in enumerate(new_list):
        for j, x in enumerate(row):
            if int(x) + m > 9:
                risk_inc = int(x) + m - 9
            else:
                risk_inc = int(x) + m
            big_list[len(new_list) * m + i] += str(risk_inc)

for i, row in enumerate(big_list):
    for m in range(1,5):
        for j, x in enumerate(row):
            if int(x) + m > 9:
                risk_inc = int(x) + m - 9
            else:
                risk_inc = int(x) + m
            big_list[i] += str(risk_inc)

path_costs = []
visited = {}
unvisited = {}

for i, row in enumerate(big_list):
    for j, x in enumerate(row):
        unvisited[str(j) + "," + str(i)] = float("inf")
unvisited["0,0"] = 0

for v in big_list:
    row_costs = []
    for w in v:
        row_costs.append(int(w))
    path_costs.append(row_costs.copy())

path_costs[0][0] = 0
unvisitheu = {}
unvisitheu["0,0"] = 0
visit_count = unvisited.copy()
directions = [[1,0],[-1,0],[0,1],[0,-1]]

rows = len(path_costs)
cols = len(path_costs[0])

count = 0
while unvisited:
    # print(count)
    count += 1
    current = min(unvisitheu, key=unvisitheu.get)
    # print(current)
    coord = current.split(",")
    for direction in directions:
        dx = int(coord[0]) + direction[0]
        dy = int(coord[1]) + direction[1]
        dxy = str(dx) + "," + str(dy)
        if dxy in unvisited.keys():
            if unvisited[dxy] > unvisited[current] + path_costs[dy][dx]:
                unvisited[dxy] = unvisited[current] + path_costs[dy][dx]
                unvisitheu[dxy] = unvisited[current] + path_costs[dy][dx] + (rows - 1 - dy) + (cols - 1 - dx)
    visited[current] = unvisited[current]
    if visit_count[current] == float("inf"):
        visit_count[current] = 1
    else:
        visit_count[current] += 1
    if current == (str(rows - 1) + "," + str(cols - 1)):
        break
    unvisited.pop(current)
    unvisitheu.pop(current)

print(visited[str(rows - 1) + "," + str(cols - 1)])

for value in visit_count:
    if visit_count[value] > 1 and visit_count[value] != float("inf"):
        print(value)