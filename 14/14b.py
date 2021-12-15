aoc_input = open("input14.txt", "r")
new_list = aoc_input.read().split("\n\n")
aoc_input.close()

poly = new_list[0]
rules = new_list[1].splitlines()

p_rules = {}
poly_count = {}

for rule in rules:
    new_rule = rule.split(" -> ")
    p_rules[new_rule[0]] = new_rule[1]

for v in p_rules.keys():
    poly_count[v] = 0

for i in range(len(poly) - 1):
    poly_count[poly[i] + poly[i + 1]] += 1

for j in range(40):
    temp_poly = poly_count.copy()
    for v in poly_count:
        if poly_count[v] > 0:
            temp_poly[v[0] + p_rules[v]] += poly_count[v]
            temp_poly[p_rules[v] + v[1]] += poly_count[v]
            temp_poly[v] -= poly_count[v]
    poly_count = temp_poly.copy()

poly_counted = {}

for v in p_rules:
    poly_counted[p_rules[v]] = 0

for v in poly_count:
    poly_counted[v[0]] += poly_count[v]
    poly_counted[v[1]] += poly_count[v]

poly_counted[poly[0]] -= 1
poly_counted[poly[-1]] -= 1

for v in poly_counted:
    poly_counted[v] /= 2

poly_counted[poly[0]] += 1
poly_counted[poly[-1]] += 1

largest = 0
smallest = poly_counted[poly[0]]
for v in poly_counted:
    if poly_counted[v] > largest:
        largest = poly_counted[v]
    if poly_counted[v] < smallest:
        smallest = poly_counted[v]

print(int(largest - smallest))