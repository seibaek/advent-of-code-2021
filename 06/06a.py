def create_list():
    aoc_input = open("input06", "r")
    new_list = aoc_input.read().split(",")
    aoc_input.close()
    return new_list

def sum_fish(input_list):
    total = 0
    for i in input_list:
        total += i
    print(total)

def day_proces(input_list):
    holder = input_list.copy()
    lantern_fish = input_list.copy()
    for i in range(80):
        for j in range(8):
            lantern_fish[7-j] = holder[8-j]
        lantern_fish[8] = holder[0]
        lantern_fish[6] += holder[0]
        holder = lantern_fish.copy()
    return lantern_fish

def sort_list(input_list):
    sorted = []
    for i in range(9):
        sorted.append(input_list.count(str(i)))
    print(sorted)
    sum_fish(day_proces(sorted))

sort_list(create_list())