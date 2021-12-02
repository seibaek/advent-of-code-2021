def solution_one_two():
    new_list = create_list()
    lista = []
    listb = []
    counter = 0
    for i in range(len(new_list)):
        if len(lista) != 3:
            lista.append(int(new_list[i]))
            listb.append(int(new_list[i + 1]))
        if len(listb) == 3:
            if sum(lista) < sum(listb):
                counter += 1
            try:
                lista = listb.copy()
                listb.append(int(new_list[i + 2]))
                listb.pop(0)
            except:
                print(counter)
                break

def create_list():
    input_list = open("inputone", "r")
    lines = input_list.read().splitlines()
    input_list.close()
    return lines

solution_one_two()






