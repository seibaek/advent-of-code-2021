# moving window
import math


#hello = [1,6,3,10,2,12,4,5,6,20,30]





def initial():
    hello = printonelines()
    lista = []
    listb = []
    counter = 0
    for i in range(len(hello)):
        if len(lista) != 3:
            lista.append(int(hello[i]))
            listb.append(int(hello[i+1]))
        if len(listb) == 3:
            if sum(lista) < sum(listb):
                counter += 1
            try:
                lista = listb.copy()
                listb.append(int(hello[i+2]))
                listb.pop(0)
#                print(lista)
#                print(listb)
            except:
                print(counter)
                break

def printonelines():
    oneinput = open("inputgithub", "r")
    lines = oneinput.read().splitlines()
    oneinput.close()
    return lines

initial()






