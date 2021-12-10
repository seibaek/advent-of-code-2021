aoc_input = open("input10", "r")
new_list = aoc_input.read().splitlines()
aoc_input.close()

print(new_list)

# [], (), {}, <>
points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
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

for line_i, line in enumerate(new_list):
    line_len = len(line)
    expected = []
    for char_i in range(line_len):
        if line[char_i] in open_opposites.keys():
            expected.append(open_opposites[line[char_i]])
        elif line[char_i] in close_opposites.keys() and line[char_i] != expected[-1]:
            score += points[line[char_i]]
            break
        else:
            expected.pop()

print(score)