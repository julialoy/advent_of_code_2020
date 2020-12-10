with open('day_9_puzzle_1_input.txt') as f:
    raw_data = f.read()
    num_lst = [int(num.strip()) for num in raw_data.split('\n')]
    target = 258585477

    cont_num_lst = []
    set_found = False
    for i in range(0, len(num_lst)-1):
        if num_lst[i] == target:
            break
        cont_num_lst.append(num_lst[i])
        for x in range(i+1, len(num_lst)-1):
            cont_num_lst.append(num_lst[x])
            if num_lst[x] == target:
                break
            elif sum(cont_num_lst) == target and len(cont_num_lst) >= 2:
                set_found = True
                print(min(cont_num_lst) + max(cont_num_lst))
                break
        if not set_found:
            cont_num_lst = []

