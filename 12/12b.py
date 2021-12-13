aoc_input = open("input12.txt", "r")
new_list = aoc_input.read().splitlines()
aoc_input.close()

for i, v in enumerate(new_list):
    new_list[i] = v.split("-")

paths = {}

for v in new_list:
    paths[v[0]] = []
    paths[v[1]] = []

for v in new_list:
    paths[v[0]].append(v[1])
    paths[v[1]].append(v[0])

possible_paths = []

begin = ["start"]

def path_finder(connections, current_path):
    for path in connections:
        this_path = current_path.copy()
        if path not in this_path and path.islower() and path != "start":
            this_path.append(path)
            if path == "end":
                possible_paths.append(this_path)
            else:
                path_finder(paths[path], this_path)
        elif path.isupper() and path != "start":
            this_path.append(path)
            if path == "end":
                possible_paths.append(this_path)
            else:
                path_finder(paths[path], this_path)
        elif not has_small_cave_repeat(this_path) and path.islower() and path != "start":
            this_path.append(path)
            if path == "end":
                possible_paths.append(this_path)
            else:
                path_finder(paths[path], this_path)

def has_small_cave_repeat(in_list):
    has_repeat = False
    for v in in_list:
        if v.islower():
            if in_list.count(v) > 1:
                has_repeat = True
    return has_repeat

path_finder(paths[begin[0]], begin)

print(len(possible_paths))
