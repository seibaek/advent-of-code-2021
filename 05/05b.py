def create_list():
    fifth_input = open("input05", "r")
    new_list = fifth_input.read().replace("\n\n", "\n").split("\n")
    fifth_input.close()
    return new_list

def process_points(input_list):
    new_list = list(filter(filter_blanks, input_list))
    atob = []
    for i, value in enumerate(new_list):
        line = value.split(' -> ')
        xandy = []
        for y in line:
            xandy.append(y.split(','))
        atob.append(xandy)
    return solution_five(atob)

def filter_blanks(input_list):
    if input_list == "":
        return False
    else:
        return True

def solution_five(input_list):
    count_list = set()
    solution_list = set()
    for h, hv in enumerate(input_list):
        x1 = hv[0][0]
        x2 = hv[1][0]
        y1 = hv[0][1]
        y2 = hv[1][1]
        if abs(int(y1) - int(y2)) > 0 and abs(int(x1) - int(x2)) == 0:
            for j in range(abs(int(y1) - int(y2))+1):
                if int(y1) < int(y2):
                    if str([x1, str(int(y1) + j)]) not in count_list:
                        count_list.add(str([x1, str(int(y1) + j)]))
                    else:
                        solution_list.add(str([x1, str(int(y1) + j)]))
                elif int(y1) > int(y2):
                    if str([x2, str(int(y2) + j)]) not in count_list:
                        count_list.add(str([x2, str(int(y2) + j)]))
                    else:
                        solution_list.add(str([x2, str(int(y2) + j)]))
        if abs(int(x1) - int(x2)) > 0 and abs(int(y1) - int(y2)) == 0:
            for j in range(abs(int(x1) - int(x2))+1):
                if int(x1) < int(x2):
                    if str([str(int(x1) + j), y1]) not in count_list:
                        count_list.add(str([str(int(x1) + j), y1]))
                    else:
                        solution_list.add(str([str(int(x1) + j), y1]))
                elif int(x1) > int(x2):
                    if str([str(int(x2) + j), y2]) not in count_list:
                        count_list.add(str([str(int(x2) + j), y2]))
                    else:
                        solution_list.add(str([str(int(x2) + j), y2]))
        if abs(int(x1) - int(x2)) > 0 and abs(int(y1) - int(y2)) > 0:
            for j in range(abs(int(y1) - int(y2)) + 1):
                if int(y1) < int(y2) and int(x1) < int(x2):
                    if str([str(int(x1) + j), str(int(y1) + j)]) not in count_list:
                        count_list.add(str([str(int(x1) + j), str(int(y1) + j)]))
                    else:
                        solution_list.add(str([str(int(x1) + j), str(int(y1) + j)]))
                if int(y2) < int(y1) and int(x1) < int(x2):
                    if str([str(int(x1) + j), str(int(y1) - j)]) not in count_list:
                        count_list.add(str([str(int(x1) + j), str(int(y1) - j)]))
                    else:
                        solution_list.add(str([str(int(x1) + j), str(int(y1) - j)]))
                if int(y1) < int(y2) and int(x2) < int(x1):
                    if str([str(int(x2) + j), str(int(y2) - j)]) not in count_list:
                        count_list.add(str([str(int(x2) + j), str(int(y2) - j)]))
                    else:
                        solution_list.add(str([str(int(x2) + j), str(int(y2) - j)]))
                if int(y2) < int(y1) and int(x2) < int(x1):
                    if str([str(int(x2) + j), str(int(y2) + j)]) not in count_list:
                        count_list.add(str([str(int(x2) + j), str(int(y2) + j)]))
                    else:
                        solution_list.add(str([str(int(x2) + j), str(int(y2) + j)]))
    print(len(solution_list))


process_points(create_list())