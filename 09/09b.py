
aoc_input = open("input09", "r")
new_list = aoc_input.read().splitlines()
aoc_input.close()
# find numbers that are ajacent to only larger numbers
line_length = len(new_list[0])
list_length = len(new_list)
final_risk_score = 0
low_list = [] # list of all lowpoints

# padding the "edges" of the input, so less checks are needed
wallnine = ""
for i in range(line_length):
    wallnine += "9"
new_list.insert(0, wallnine)
new_list.append(wallnine)
for row_i, list_v in enumerate(new_list):
    new_list[row_i] = "9" + list_v + "9"

# recalculate lengths based on the new padded list
line_length = len(new_list[0])
list_length = len(new_list)

# from PART 1 with minor changes to create a list ("low_list") of the low points

for row_i, list_v in enumerate(new_list):
    # solves for inner rows
    if row_i != 0 and row_i != list_length - 1:
        for num_i, num_v in enumerate(list_v):
            if num_i != 0 and num_i != line_length - 1:
                if int(num_v) < int(list_v[num_i + 1]) and int(num_v) < int(list_v[num_i - 1]) and int(num_v) < int(new_list[row_i - 1][num_i]) and int(num_v) < int(new_list[row_i + 1][num_i]):
                    final_risk_score += int(num_v) + 1
                    low_list.append([row_i,num_i])
            if num_i == 0:
                if int(num_v) < int(list_v[num_i + 1]) and int(num_v) < int(new_list[row_i - 1][num_i]) and int(num_v) < int(new_list[row_i + 1][num_i]):
                    final_risk_score += int(num_v) + 1
                    low_list.append([row_i, num_i])
            if num_i == list_length -1:
                if int(num_v) < int(list_v[num_i - 1]) and int(num_v) < int(new_list[row_i - 1][num_i]) and int(num_v) < int(new_list[row_i + 1][num_i]):
                    final_risk_score += int(num_v) + 1
                    low_list.append([row_i, num_i])
    # solves for first row
    if row_i == 0:
        for num_i, num_v in enumerate(list_v):
            if num_i != 0 and num_i != line_length - 1:
                if int(num_v) < int(list_v[num_i + 1]) and int(num_v) < int(list_v[num_i - 1]) and int(num_v) < int(new_list[row_i + 1][num_i]):
                    final_risk_score += int(num_v) + 1
                    low_list.append([row_i, num_i])
            if num_i == 0:
                if int(num_v) < int(list_v[num_i + 1]) and int(num_v) < int(new_list[row_i + 1][num_i]):
                    final_risk_score += int(num_v) + 1
                    low_list.append([row_i, num_i])
            if num_i == list_length -1:
                if int(num_v) < int(list_v[num_i - 1]) and int(num_v) < int(new_list[row_i + 1][num_i]):
                    final_risk_score += int(num_v) + 1
                    low_list.append([row_i, num_i])
    # solves for final row
    if row_i == list_length - 1:
        for num_i, num_v in enumerate(list_v):
            if num_i != 0 and num_i != line_length - 1:
                if int(num_v) < int(list_v[num_i + 1]) and int(num_v) < int(list_v[num_i - 1]) and int(num_v) < int(new_list[row_i - 1][num_i]):
                    final_risk_score += int(num_v) + 1
                    low_list.append([row_i, num_i])
            if num_i == 0:
                if int(num_v) < int(list_v[num_i + 1]) and int(num_v) < int(new_list[row_i - 1][num_i]):
                    final_risk_score += int(num_v) + 1
                    low_list.append([row_i, num_i])
            if num_i == list_length -1:
                if int(num_v) < int(list_v[num_i - 1]) and int(num_v) < int(new_list[row_i - 1][num_i]):
                    final_risk_score += int(num_v) + 1
                    low_list.append([row_i, num_i])

# PART TWO BEGINS HERE

top_three = [0,0,0] # list to hold the 3 largest basins
basin_points = set() # using a set to hold each point of the current basin being measured, using a set because it can only hold unique values

# recursive function to measure basin size, takes the low point as an argument
# checks neighbouring points to see if this is an edge ("9")
# checks neighbouring points against the "basin_points" set to see if this is a new point
# finally checks the total size of the basin and compares to keep if it's bigger than current top 3 (top_three)
def each_point(low_point):
    global basin_points
    adjacents = [] # holds a list of the adjacent points to the current point
    x = int(low_point[0]) # x coordinate of the point
    y = int(low_point[1]) # y coordinate of the point
    if new_list[x - 1][y] != "9": # check to the left
        if str([x - 1, y]) not in basin_points:
            adjacents.append([str(x - 1), str(y)])
            basin_points.add(str([x - 1, y]))
    if new_list[x + 1][y] != "9": # check to the right
        if str([x + 1, y]) not in basin_points:
            adjacents.append([str(x + 1), str(y)])
            basin_points.add(str([x + 1, y]))
    if new_list[x][y - 1] != "9": # check above
        if str([x, y - 1]) not in basin_points:
            adjacents.append([str(x), str(y - 1)])
            basin_points.add(str([x, y - 1]))
    if new_list[x][y + 1] != "9": # check below
        if str([x, y + 1]) not in basin_points:
            adjacents.append([str(x), str(y + 1)])
            basin_points.add(str([x, y + 1]))
    if len(adjacents) > 0: # if there's more adjacent points continue calling itself for each point(recursive function)
        for point in adjacents:
            each_point(point)

def init_check_adjacents(input_list):
    global top_three
    global basin_points
    for low_point in input_list: # for each low point
        basin_points.clear() # refresh for each new basin check
        each_point(low_point) # recursive func call
        basin_size = len(basin_points) # the total size of the basin

        # keep only the biggest 3 basin sizes
        top_three.append(basin_size)
        top_three.sort(reverse=True)
        top_three.pop()

init_check_adjacents(low_list)


# print solution:
print(top_three[0] * top_three[1] * top_three[2])


