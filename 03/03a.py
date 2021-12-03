one = []
zero = []

def create_list():
    third_input = open("input03", "r")
    new_list = third_input.read().splitlines()
    third_input.close()
    return new_list

def count_binary(input_list):
    bin_len = len(input_list[0])
    final_binary = ''
    for i in range(bin_len):
        one = 0
        zero = 0
        for item in input_list:
            if item[i] == '1':
                one += 1
            else:
                zero += 1
        if one > zero:
            final_binary += '1'
        else:
            final_binary += '0'
    return final_binary

def third_solution(binary_input):
    value1 = int(binary_input,2)
    value2 = ''
    for x in binary_input:
        if x == '1':
            value2 += '0'
        else:
            value2 += '1'
    print(value1 * int(value2,2))


third_solution(count_binary(create_list()))