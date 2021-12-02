def create_list():
    thirdinput = open("input02", "r")
    new_list = thirdinput.read().splitlines()
    thirdinput.close()
    return new_list

def convert_list(input_list):
    for i in range(len(input_list)):
        input_list[i] = input_list[i].split()
        input_list[i][1] = int(input_list[i][1])
    return input_list

def sub_movement(input_new_list):
    x = 0
    y = 0
    for move in input_new_list:
        if move[0] == "down":
            y += move[1]
        elif move[0] == "up":
            y -= move[1]
        else:
            x += move[1]
    final_value = x * y
    return final_value


print(sub_movement(convert_list(create_list())))