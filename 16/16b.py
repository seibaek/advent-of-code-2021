aoc_input = open("input16.txt", "r")
input_string = aoc_input.read()
aoc_input.close()

print(input_string)

new_string = ""

hex_dic = {
    "0000":"0",
    "0001":"1",
    "0010":"2",
    "0011":"3",
    "0100":"4",
    "0101":"5",
    "0110":"6",
    "0111":"7",
    "1000":"8",
    "1001":"9",
    "1010":"A",
    "1011":"B",
    "1100":"C",
    "1101":"D",
    "1110":"E",
    "1111":"F",
}
bin_dic = {
    "0":"0000",
    "1":"0001",
    "2":"0010",
    "3":"0011",
    "4":"0100",
    "5":"0101",
    "6":"0110",
    "7":"0111",
    "8":"1000",
    "9":"1001",
    "A":"1010",
    "B":"1011",
    "C":"1100",
    "D":"1101",
    "E":"1110",
    "F":"1111",
}
op_dic = {
    "0":"sum",
    "1":"product",
    "2":"min",
    "3":"max",
    "5":"greaterthan",
    "6":"lessthan",
    "7":"equal to",
}

for v in input_string:
    if v != "\n":
        new_string += bin_dic[v]

print(new_string)

version_total = 0

def decode(in_string):
    print(in_string)
    if in_string is None:
        return
    if len(in_string) < 3:
        return
    if int(in_string) < 1:
        return
    V = in_string[:3]
    # print(V)
    global version_total
    version_total += int(V, 2)
    T = in_string[3:6]
    # print(T)
    TID = (hex_dic["0" + T])
    if TID != "4":
        I = in_string[6]
        if I == "0": # total length of bits
            L = int(in_string[7:22], 2)
            decode(in_string[22:])
        else: # number of sub-packets
            L = int(in_string[7:18], 2)
            decode(in_string[18:])
    else:
        out_string = in_string[6:]
        decode(literal(out_string))

def literal(in_string):
    if in_string[0] == "1":
        return literal(in_string[5:])
    # bin_int = int(in_string[1:5], 2)
    else:
        return in_string[5:]

def operator(in_string):
    if in_string[0] == "0":
        L = int(in_string[7:22], 2)
        decode(in_string[22:L])
    else:  # number of sub-packets
        L = int(in_string[7:18], 2)
        decode(in_string[18:])
decode(new_string)

print(version_total)