aoc_input = open("input13.txt", "r")
new_list = aoc_input.read().split("\n\n")
aoc_input.close()

points = new_list[0].splitlines()
folds = new_list[1].splitlines()

for i,v in enumerate(folds):
    folds[i] = v.split("=")
    folds[i][0] = folds[i][0][-1]

for i,v in enumerate(points):
    points[i] = v.split(",")

solution_set = set()

def folder(fold, axis):
    global solution_set
    folded_points = points.copy()
    solution_set.clear()
    if axis == "x":
        for i, v in enumerate(points):
            if int(v[0]) > int(fold):
                folded_points[i][0] = str(int(fold) + int(fold) - int(v[0]))
    elif axis == "y":
        for i, v in enumerate(points):
            if int(v[1]) > int(fold):
                folded_points[i][1] = str(int(fold) + int(fold) - int(v[1]))
    for j in folded_points:
        solution_set.add(j[0] + "," + j[1])

for i in range(len(folds)):
    folder(folds[i][1], folds[i][0])
    points.clear()
    for v in solution_set:
        points.append(v.split(","))

xlen = 0
ylen = 0
for v in solution_set:
    holder = v.split(",")
    if int(holder[0]) > xlen:
        xlen = int(holder[0])
    if int(holder[1]) > ylen:
        ylen = int(holder[1])

row = []
for i in range(xlen + 1):
    row.append(".")

matrix = []
for i in range(ylen + 1):
    matrix.append(row.copy())

for v in solution_set:
    coord = v.split(",")
    matrix[int(coord[1])][int(coord[0])] = "#"

for h in matrix:
    print(h)
