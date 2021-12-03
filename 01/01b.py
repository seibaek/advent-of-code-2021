def create_list():
    input_list = open("01/input01", "r")
    new_list = input_list.read().splitlines()
    input_list.close()
    return new_list

def part_two():
    input_values = create_list()
    list_a = []
    list_b = []
    counter = 0
    for i in range(len(input_values)):
        if len(list_a) != 3:
            list_a.append(int(input_values[i]))
            list_b.append(int(input_values[i + 1]))
        if len(list_b) == 3:
            if sum(list_a) < sum(list_b):
                counter += 1
            try:
                list_a = list_b.copy()
                list_b.append(int(input_values[i + 2]))
                list_b.pop(0)
            except:
                return counter

print(part_two())






