aoc_input = open("input08", "r")
new_list = aoc_input.read().splitlines()
aoc_input.close()

for i, v in enumerate(new_list):
    new_list[i] = v.split(" | ")

counter = 0

for i in new_list:
    split_output = i[1].split(" ")
    for j in split_output:
        x = len(j)
        if x == 2 or x == 4 or x == 3 or x == 7:
            counter += 1

print(counter)