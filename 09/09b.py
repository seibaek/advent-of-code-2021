
aoc_input = open("input09", "r")
new_list = aoc_input.read().splitlines()
aoc_input.close()


# find numbers that are ajacent to only larger numbers
line_length = len(new_list[0])
list_length = len(new_list)
final_risk_score = 0
low_list = [] # list of all lowpoints

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

print(low_list)
total_size = 0
def check_adjacents(input_list):
    global total_size
    for low_point in input_list:
        adjacents = []
        if new_list[int(low_point[0]) - 1][int(low_point[1])] != "9":
            adjacents.append([int(low_point[0]) - 1, int(low_point[1])])
        if new_list[int(low_point[0]) + 1][int(low_point[1])] != "9":
            adjacents.append([int(low_point[0]) + 1, int(low_point[1])])
        if new_list[int(low_point[0])][int(low_point[1]) - 1] != "9":
            adjacents.append([int(low_point[0]), int(low_point[1] + 1)])
        if new_list[int(low_point[0])][int(low_point[1]) + 1] != "9":
            adjacents.append([int(low_point[0]), int(low_point[1] + 1)])
    if len(adjacents) == 0:
        return total_score
check_adjacents(low_list)

# go through low points
# find adjacent points
# check if adjacent points are nines
# if adjacent point is not a nine +1 to temporary basin area
# repeat with adjacent points
# finish each iteration when theres no more points in list[]

