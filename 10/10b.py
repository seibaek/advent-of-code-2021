aoc_input = open("input10", "r")
new_list = aoc_input.read().splitlines()
aoc_input.close()

# [], (), {}, <>
points = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}
close_opposites = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<"
}
open_opposites = {
    "(":")",
    "[":"]",
    "{":"}",
    "<":">"
}

score = 0
incompletes = []

def calculate_incompletes(input_list):
    line_score = 0
    reversed_list = input_list.copy()
    reversed_list.reverse()
    for closer in reversed_list:
        line_score = (line_score * 5) + points[closer]
    return line_score

for line_i, line in enumerate(new_list):
    line_len = len(line)
    expected = []
    for char_i in range(line_len):
        if line[char_i] in open_opposites.keys(): # if character is a opener
            expected.append(open_opposites[line[char_i]])
            if char_i == line_len - 1:
                incompletes.append(calculate_incompletes(expected))
        elif line[char_i] in close_opposites.keys() and line[char_i] != expected[-1]: # if character is illegal closer
            score += points[line[char_i]]
            break
        else: # if character is legal closer
            expected.pop()
            if char_i == line_len - 1:
                incompletes.append(calculate_incompletes(expected))

incompletes.sort()
print(incompletes[len(incompletes)//2])