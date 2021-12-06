# counter = 0

def create_list():
    fifth_input = open("input05", "r")
    new_list = fifth_input.read().replace("\n\n", "\n").split("\n")
    fifth_input.close()
    return new_list

def process_points(input_list):
    new_list = list(filter(filter_blanks, input_list))
    # print(len(new_list))
    atob = []
    for i, value in enumerate(new_list):
        line = value.split(' -> ')
        xandy = []
        for y in line:
            xandy.append(y.split(','))
        atob.append(xandy)
    # print(atob)
    return solution_five(atob)

def filter_blanks(input_list):
    if input_list == "":
        return False
    else:
        return True

def solution_five(input_list):
    count_list = []
    # solution_list = []
    counter = 0
    for h, hv in enumerate(input_list):
        # print(hv[0][1])
        # print(hv[1][1])
        count_list.append(hv[0])
        count_list.append(hv[1])
        x1 = hv[0][0]
        x2 = hv[1][0]
        y1 = hv[0][1]
        y2 = hv[1][1]
        if abs(int(y1) - int(y2)) > 0:
        #     # print(abs(int(y1) - int(y2)))
            for j in range(abs(int(y1) - int(y2)) - 1):
                if int(y1) < int(y2):
                    if count_list.count([y2, str(int(x2) + j + 1)]) == 1:
                        counter += 1
                    count_list.append([x1, str(int(y1) + j + 1)])
                else:
                    if count_list.count([str(int(y2) + j + 1), x2]) == 1:
                        counter += 1
                    count_list.append([x2, str(int(y2) + j + 1)])
        if abs(int(x1) - int(x2)) > 0:
            for j in range(abs(int(x1) - int(x2)) - 1):
                if int(x1) < int(x2):
                    if count_list.count([y1, str(int(x1) + j + 1)]) == 1:
                        counter += 1
                    count_list.append([y1, str(int(x1) + j + 1)])
                else:
                    if count_list.count([y2, str(int(x2) + j + 1)]) == 1:
                        counter += 1
                    count_list.append([y2, str(int(x2) + j + 1)])
    print(counter)
    print("hello")

process_points(create_list())

