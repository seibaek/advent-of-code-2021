aoc_input = open("input15.txt", "r")
new_list = aoc_input.read().splitlines()
aoc_input.close()

path_costs = []
visited = {}
unvisited = {}

for i, row in enumerate(new_list):
    for j, x in enumerate(row):
        unvisited[str(j) + "," + str(i)] = float("inf")
unvisited["0,0"] = 0

for v in new_list:
    row_costs = []
    for w in v:
        row_costs.append(int(w))
    path_costs.append(row_costs.copy())

path_costs[0][0] = 0

directions = [[1,0],[-1,0],[0,1],[0,-1]]

while unvisited:
    current = min(unvisited, key=unvisited.get)
    coord = current.split(",")
    for direction in directions:
        dx = int(coord[0]) + direction[0]
        dy = int(coord[1]) + direction[1]
        dxy = str(dx) + "," + str(dy)
        if dxy in unvisited.keys():
            if unvisited[dxy] > unvisited[current] + path_costs[dy][dx]:
                unvisited[dxy] = unvisited[current] + path_costs[dy][dx]
    visited[current] = unvisited[current]
    unvisited.pop(current)

rows = len(path_costs)
cols = len(path_costs[0])
print(visited[str(rows - 1) + "," + str(cols - 1)])