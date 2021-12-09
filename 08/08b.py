# Parse advent of code challenge input into a list
aoc_input = open("input08", "r")
new_list = aoc_input.read().splitlines()
aoc_input.close()

# Separate the crytopgraphic inputs and outputs into their own list and nesting them in the same list index
for i, v in enumerate(new_list):
    new_list[i] = v.split(" | ")

# define the solution variables,
# grand_total is the final answer
grand_total = 0
# digital number holds the solution key for the current input
# as a letter becomes deciphered for a specific segment,
# the letter is placed in this variable for the index corresponding to the segment
digital_number = [0,0,0,0,0,0,0]
# digimon variable acts as a binary list reference key
# the index in the list represents each of the segments
# each binary bit represents a segment being active (1) or inactive (0)
digimon = [
    [1,0,1,1,1,1,1], #zero
    [0,0,0,0,1,0,1], #one
    [1,1,1,0,1,1,0], #two
    [1,1,1,0,1,0,1], #three
    [0,1,0,1,1,0,1], #four
    [1,1,1,1,0,0,1], #five
    [1,1,1,1,0,1,1], #six
    [1,0,0,0,1,0,1], #seven
    [1,1,1,1,1,1,1], #eight
    [1,1,1,1,1,0,1]  #nine
]

# checks an argument against "digital_number" to see if the letter has already been decyphered or not
def digi_check(input_letter):
    if input_letter not in digital_number:
        return True
    else:
        return False

# the main function that loops through each input value and decypher each segment letter
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

# decode function decyphers a combination of letters into its corresponding digit
# for each letter in the input sequence of letters, store the corresponding binary bit in code_number
# compares the final code binary list  to digimon variable and returns the matching index in the binary list
def decode(input_list):
    code_number = [0,0,0,0,0,0,0]
    for v in input_list:
        code_number[digital_number.index(v)] = 1
    return digimon.index(code_number)

# the integer produced from decode function is added to a string forming the final decyphered number for this iteration
# the final number for each iteration is added to the grand_total variable
def accumulate(input_list):
    accu_list = input_list.split(" ")
    output_number = ""
    global grand_total
    for v in accu_list:
        output_number += str(decode(v))
    grand_total += int(output_number)

# main function call
for each_set in new_list:
    solve(each_set[0], each_set[1])

# prints the grand_total which is the final answer/solution
print(grand_total)