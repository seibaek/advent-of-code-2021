
aoc_input = open("input09", "r")
new_list = aoc_input.read().splitlines()
aoc_input.close()


# find numbers that are ajacent to only larger numbers
line_length = len(new_list[0])
list_length = len(new_list)
final_risk_score = 0

for row_i, list_v in enumerate(new_list):
    # solves for inner rows
    if row_i != 0 and row_i != list_length - 1:
        for num_i, num_v in enumerate(list_v):
            if num_i != 0 and num_i != line_length - 1:
                if int(num_v) < int(list_v[num_i + 1]) and int(num_v) < int(list_v[num_i - 1]) and int(num_v) < int(new_list[row_i - 1][num_i]) and int(num_v) < int(new_list[row_i + 1][num_i]):
                    final_risk_score += int(num_v) + 1
            if num_i == 0:
                if int(num_v) < int(list_v[num_i + 1]) and int(num_v) < int(new_list[row_i - 1][num_i]) and int(num_v) < int(new_list[row_i + 1][num_i]):
                    final_risk_score += int(num_v) + 1
            if num_i == list_length -1:
                if int(num_v) < int(list_v[num_i - 1]) and int(num_v) < int(new_list[row_i - 1][num_i]) and int(num_v) < int(new_list[row_i + 1][num_i]):
                    final_risk_score += int(num_v) + 1
    # solves for first row
    if row_i == 0:
        for num_i, num_v in enumerate(list_v):
            if num_i != 0 and num_i != line_length - 1:
                if int(num_v) < int(list_v[num_i + 1]) and int(num_v) < int(list_v[num_i - 1]) and int(num_v) < int(new_list[row_i + 1][num_i]):
                    final_risk_score += int(num_v) + 1
            if num_i == 0:
                if int(num_v) < int(list_v[num_i + 1]) and int(num_v) < int(new_list[row_i + 1][num_i]):
                    final_risk_score += int(num_v) + 1
            if num_i == list_length -1:
                if int(num_v) < int(list_v[num_i - 1]) and int(num_v) < int(new_list[row_i + 1][num_i]):
                    final_risk_score += int(num_v) + 1
    # solves for final row
    if row_i == list_length - 1:
        for num_i, num_v in enumerate(list_v):
            if num_i != 0 and num_i != line_length - 1:
                if int(num_v) < int(list_v[num_i + 1]) and int(num_v) < int(list_v[num_i - 1]) and int(num_v) < int(new_list[row_i - 1][num_i]):
                    final_risk_score += int(num_v) + 1
            if num_i == 0:
                if int(num_v) < int(list_v[num_i + 1]) and int(num_v) < int(new_list[row_i - 1][num_i]):
                    final_risk_score += int(num_v) + 1
            if num_i == list_length -1:
                if int(num_v) < int(list_v[num_i - 1]) and int(num_v) < int(new_list[row_i - 1][num_i]):
                    final_risk_score += int(num_v) + 1



print(final_risk_score)