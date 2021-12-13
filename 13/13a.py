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
    if axis == "x":
        for i,v in enumerate(points):
            if int(v[0]) > int(fold):
                folded_points[i][0] = str(int(fold) + int(fold) - int(v[0]))
            if v[0] == fold:
                folded_points.pop(i)
    elif axis == "y":
        for i,v in enumerate(points):
            if int(v[1]) > int(fold):
                folded_points[i][1] = str(int(fold) + int(fold) - int(v[1]))
            if v[1] == fold:
                folded_points.pop(i)
    for v in folded_points:
        solution_set.add(v[0] + "," + v[1])

folder(folds[0][1], folds[0][0])

print(len(solution_set))
