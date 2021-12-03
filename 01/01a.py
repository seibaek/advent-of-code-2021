def count_increase(input_list):
    old = None
    counter = 0
    for x in input_list:
        if old != None:
            if int(x) > old:
                counter += 1
        old = int(x)
    return counter

def create_list():
    oneinput = open("01/input01", "r")
    lines = oneinput.read().splitlines()
    oneinput.close()
    return lines


def one_solution():
    y = create_list()
    print(count_increase(y))

one_solution()
