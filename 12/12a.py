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

print(paths)

possible_paths = []

begin = ["start"]


# Create function using first point
# for each connection
# recursive
# exit if no more connections available
# exit if end is reached
# if ended add to path list

def path_finder(connections, current_path):
    for path in connections:
        this_path = current_path.copy()
        if path not in this_path and not path.isupper() and path != "start":
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

path_finder(paths[begin[0]], begin)

print(len(possible_paths))