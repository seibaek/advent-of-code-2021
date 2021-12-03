def create_list():
    third_input = open("input03", "r")
    new_list = third_input.read().splitlines()
    third_input.close()
    return new_list

def somefun(input_list, index, bin_value):
    if len(input_list) > 1:
        smaller_list = compare_binary(input_list, index, bin_value)
        somefun(smaller_list, index + 1, bin_value)
    else:
        print(input_list)
        return ggg

def compare_binary(input_list, index, bin_value):
    # print(index)
    # print(input_list)
    one = 0
    zero = 0
    for item in input_list:
        if item[index] == '1':
            one += 1
        else:
            zero += 1
    if one >= zero:
        x = strip_list(input_list, '1', index)
        return x
    else:
        x = strip_list(input_list, '0', index)
        return x

def strip_list(input_list, value, index):
    stripped_list = []
    # print(index)
    # print(input_list)
    for item in input_list:
        if item[index] == value:
            stripped_list.append(item)
    return stripped_list

def solution_three():
    oxygen = []
    carbondioxide = []
    input_list = create_list().copy()
    animal = somefun(input_list,0,0)
    print(animal)
    print("party")

solution_three()