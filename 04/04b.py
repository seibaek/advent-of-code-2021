def create_list():
    fourth_input = open("input04", "r")
    new_list = fourth_input.read().replace("\n\n", "\n").split("\n")
    fourth_input.close()
    return new_list

def split_input(input_list):
    bingo_draw = input_list[0].split(",")
    print("space")
    boards = []
    board_group = []
    for i in range(len(input_list)-1):
        boards.append(input_list[i+1].split("\n"))
    boards.pop()
    for i, value in enumerate(boards):
        boards[i] = value[0].split(' ')
        boards[i] = list(filter(filter_blanks, boards[i]))
    for i in range(int(len(boards)/5)):
        board_group.append([])
        for j in range(5):
            board_group[i].append(boards.pop())
    board_group.reverse()
    boards = board_group.copy()
    for h, hvalue in enumerate(boards):
        column = []
        for i, ivalue in enumerate(hvalue):
            column.append([])
            for j, jvalue in enumerate(ivalue):
                column[i].insert(j,jvalue)
        boards[h].extend(column)
        column.clear()
    return bingo_coordinator(bingo_draw, boards)

def bingo_coordinator(bingo_draw, boards):
    winners = []
    for value in bingo_draw:
        for h, hvalue in enumerate(boards):
            for i, ivalue in enumerate(hvalue):
                for j, jvalue in enumerate(ivalue):
                    if jvalue == value:
                        boards[h][i][j] = 'x'
                        if boards[h][i].count('x') == 5:
                            if boards[h] not in winners:
                                winners.append(boards[h])
                            if len(winners) == len(boards) - 1:
                                return fourth_solution(boards[h], value)

def filter_blanks(input_list):
    if input_list == "":
        return False
    else:
        return True

def fourth_solution(input_list, bingo_value):
    solution_list = input_list.copy()
    sum_answer = 0
    for i in range(5):
        solution_list.pop()
    for h in solution_list:
        for i in h:
            if i != 'x':
                sum_answer += int(i)
    answer = sum_answer * int(bingo_value)
    print(answer)


split_input(create_list())


