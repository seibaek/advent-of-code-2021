aoc_input = open("input14.txt", "r")
new_list = aoc_input.read().split("\n\n")
aoc_input.close()

poly = new_list[0].splitlines()
rules = new_list[1].splitlines()

print(poly)
print(rules)
# print(new_list)

p_rules = {}

for rule in rules:
    new_rule = rule.split(" -> ")
    p_rules[new_rule[0]] = new_rule[1]

print(p_rules)

stepped = 0
def steps(in_string):
    global stepped
    stepped += 1
    print(len(in_string))
    new_string = in_string[0]
    # insert_list = []
    if stepped < 11:
        for i in range(len(in_string) - 1):
            # insert_list.append(p_rules[in_string[i] + in_string[i + 1]])
            new_string += p_rules[in_string[i] + in_string[i + 1]] + in_string[i + 1]
        return steps(new_string)
    else:
        return in_string






newest_string = steps(poly[0])


largest = 0
smallest = 10000000
a_set = set()
for chara in poly[0]:
    a_set.add(chara)

print(a_set)
for chara in a_set:
    if newest_string.count(chara) > largest:
        largest = newest_string.count(chara)
        # print(chara)
    if newest_string.count(chara) < smallest:
        smallest = newest_string.count(chara)
        # print(chara)

print(largest - smallest) # 3697, 6, 11, 15, 38, 87, 200
# print(largest) # N 4605, 7, 13, 22, 52, 118, 259
# print(smallest) # K 908, 1, 2, 7, 14, 31, 59