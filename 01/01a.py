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
    oneinput = open("input01", "r")
    lines = oneinput.read().splitlines()
    oneinput.close()
    return lines


def onesolution():
    y = printonelines()
    print(throughlist(y))

onesolution()
