aoc_input = open("input08", "r")
new_list = aoc_input.read().splitlines()
aoc_input.close()

for i, v in enumerate(new_list):
    new_list[i] = v.split(" | ")

grand_total = 0
digital_number = [0,0,0,0,0,0,0]
digimon = [[1,0,1,1,1,1,1],[0,0,0,0,1,0,1],[1,1,1,0,1,1,0],[1,1,1,0,1,0,1],[0,1,0,1,1,0,1],[1,1,1,1,0,0,1],[1,1,1,1,0,1,1],[1,0,0,0,1,0,1],[1,1,1,1,1,1,1],[1,1,1,1,1,0,1]]

def digi_check(input_letter):
    if input_letter not in digital_number:
        return True
    else:
        return False

def solve(input_list, another_list):
    solve_list = input_list.split(" ")
    global digital_number
    digital_number = [0, 0, 0, 0, 0, 0, 0]
    one = ""
    four = ""
    seven = ""
    eight = ""
    five_seg = []
    five_seg_temp = ""
    five_to_four = []
    six_seg = []
    six_seg_temp = ""
    for v in solve_list:
        if len(v) == 2:
            one = v
        elif len(v) == 4:
            four = v
        elif len(v) == 3:
            seven = v
        elif len(v) == 7:
            eight = v
        elif len(v) == 5:
            five_seg.append(v)
        elif len(v) == 6:
            six_seg.append(v)
    for v in seven:
        if one.count(v) < 1:
            digital_number[0] = v
    for v in five_seg:
        if digi_check(v):
            five_seg_temp += v
    for letter in five_seg_temp:
        if five_seg_temp.count(letter) == 1:
            five_to_four.append(letter)
    for letter in five_to_four:
        if four.count(letter) > 0:
            digital_number[3] = letter
    for m in four:
        if digi_check(m):
            if one.count(m) < 1:
                digital_number[1] = m
    for letter in five_to_four:
        if digi_check(letter):
            digital_number[5] = letter
    for letter in eight:
        if letter not in one and digi_check(letter):
            digital_number[2] = letter
    for v in six_seg:
        six_seg_temp += v
    for letter in six_seg_temp:
        if six_seg_temp.count(letter) > 2 and digi_check(letter):
            digital_number[6] = letter
        if six_seg_temp.count(letter) == 2 and digi_check(letter):
            digital_number[4] = letter
    accumulate(another_list)

def decode(input_list):
    code_number = [0,0,0,0,0,0,0]
    for v in input_list:
        code_number[digital_number.index(v)] = 1
    return digimon.index(code_number)

def accumulate(input_list):
    accu_list = input_list.split(" ")
    output_number = ""
    global grand_total
    for v in accu_list:
        output_number += str(decode(v))
    grand_total += int(output_number)

for each_set in new_list:
    solve(each_set[0], each_set[1])

print(grand_total)