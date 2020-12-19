num_dict = {8: [1], 0: [2], 17: [3], 4: [4], 1: [5], 12: [6]}
turn = 7
last_num = 12
while turn < 30000001:

    if last_num in num_dict.keys() and len(num_dict[last_num]) >= 2:
        new_num = num_dict[last_num][1] - num_dict[last_num][0]
        if new_num in num_dict.keys():
            num_dict[new_num].append(turn)
        else:
            num_dict[new_num] = [turn]
        if len(num_dict[new_num]) > 2:
            num_dict[new_num] = num_dict[new_num][1:]
    else:
        new_num = 0
        if new_num in num_dict.keys():
            num_dict[new_num].append(turn)
        else:
            num_dict[new_num] = [turn]
        if len(num_dict[new_num]) > 2:
            num_dict[new_num] = num_dict[new_num][1:]

    last_num = new_num

    turn += 1

for k, v in num_dict.items():
    if 30000000 in v:
        print(k)
