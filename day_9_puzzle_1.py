with open('day_9_puzzle_1_input.txt') as f:
    raw_data = f.read()
    num_lst = [int(num.strip()) for num in raw_data.split('\n')]

    for i in range(25, len(num_lst)):
        target = num_lst[i]
        valid_combo_found = False
        for x in range(i-25, i):
            curr_num = num_lst[x]
            for y in range(i-25, i):
                if x == num_lst[y]:
                    continue
                if curr_num + num_lst[y] == target:
                    valid_combo_found = True
                    break

        if not valid_combo_found:
            print(target)
            break
