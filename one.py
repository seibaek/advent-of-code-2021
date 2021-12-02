


def throughlist(onelist):
    old = None
    counter = 0
    for x in onelist:
        if old != None:
            if int(x) > old:
                #print(x + " is greater than " + str(old))
                counter += 1
        old = int(x)
    return counter

def printonelines():
    oneinput = open("inputgithub", "r")
    lines = oneinput.read().splitlines()
    oneinput.close()
    return lines


def onesolution():
    y = printonelines()
    print(throughlist(y))

onesolution()
