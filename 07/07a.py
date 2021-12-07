def create_list():
    aoc_input = open("input07", "r")
    new_list = aoc_input.read().replace('\n','').split(",")
    aoc_input.close()
    return new_list

def sort_list(input_list):
    sorted = []
    for i in input_list:
        sorted.append(int(i))
    sorted.sort()
    max = sorted[len(sorted)-1]
    return solution_seven(sorted, max)

def solution_seven(input_list, max):
    final_distances = []
    for position in range(max+1):
        pos_total = 0
        for crab in input_list:
            pos_total += abs(position - crab)
        final_distances.append(pos_total)
    final_distances.sort()
    return final_distances[0]

print(sort_list(create_list()))