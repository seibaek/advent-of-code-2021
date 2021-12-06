def create_list():
    third_input = open("input03", "r")
    new_list = third_input.read().splitlines()
    third_input.close()
    return new_list

def somefun(input_list, index, bin_value):
    if len(input_list) > 1:
        smaller_list = compare_binary(input_list, index, bin_value)
        return somefun(smaller_list, index + 1, bin_value)
    else:
        return input_list

def compare_binary(input_list, index, bin_value):
    one = 0
    zero = 0
    for item in input_list:
        if item[index] == '1':
            one += 1
        else:
            zero += 1
    if one >= zero and bin_value == '1':
        return strip_list(input_list, '1', index)
    elif one >= zero and bin_value == '0':
        return strip_list(input_list, '0', index)
    elif zero > one and bin_value == '0':
        return strip_list(input_list, '1', index)
    else:
        return strip_list(input_list, '0', index)

def strip_list(input_list, value, index):
    stripped_list = []
    for item in input_list:
        if item[index] == value:
            stripped_list.append(item)
    return stripped_list

def solution_three():
    input_list = create_list().copy()
    oxygen = somefun(input_list,0,'1')
    carbondioxide = somefun(input_list,0,'0')
    return int(oxygen[0],2) * int(carbondioxide[0],2)

print(solution_three())