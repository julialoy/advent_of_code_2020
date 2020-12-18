from itertools import permutations
import re


def get_perms(num_x):
    x_lst = ['X' for _ in range(0, num_x)]
    # print(len(x_lst))

    perm_str_lst = []
    for i in range(0, len(x_lst)):
        temp_lst = ['0' for _ in x_lst]
        temp_lst[i] = '1'
        perm_str_lst.append(temp_lst)

    for i in range(0, len(x_lst)):
        temp_lst = ['1' for _ in x_lst]
        temp_lst[i] = '0'
        perm_str_lst.append(temp_lst)

    temp_lst_ones_odds = ['0' if i % 2 == 0 else '1' for i in range(0, len(x_lst))]
    perm_str_lst.append(temp_lst_ones_odds)
    temp_lst_ones_evens = ['0' if i % 2 != 0 else '1' for i in range(0, len(x_lst))]
    perm_str_lst.append(temp_lst_ones_evens)
    temp_lst_zeros_odds = ['1' if i % 2 == 0 else '0' for i in range(0, len(x_lst))]
    perm_str_lst.append(temp_lst_zeros_odds)
    temp_lst_zeros_evens = ['1' if i % 2 != 0 else '0' for i in range(0, len(x_lst))]
    perm_str_lst.append(temp_lst_zeros_evens)

    for i in range(1, len(x_lst)):
        temp_lst_ones = ['1' for _ in x_lst]
        temp_lst_zeros = ['0' for _ in x_lst]
        for j in range(0, len(x_lst)):
            if j % i == 0:
                temp_lst_ones[j] = '0'
                temp_lst_zeros[j] = '1'
            perm_str_lst.append(temp_lst_zeros)
            perm_str_lst.append(temp_lst_ones)

    perm_str_lst.append(['1' for _ in range(0, len(x_lst))])
    perm_str_lst.append(['0' for _ in range(0, len(x_lst))])

    unique_perm_str_lst = []
    for str_lst in perm_str_lst:
        if str_lst not in unique_perm_str_lst:
            unique_perm_str_lst.append(str_lst)

    perms_lst = []

    for unique_perm in unique_perm_str_lst:
        perms = [p for p in permutations(''.join(unique_perm), len(x_lst))]
        for perm in perms:
            if perm not in perms_lst:
                perms_lst.append(perm)

    print(f"Num perms: {len(perms_lst)}")
    return perms_lst


with open('day_14_puzzle_1_input.txt') as f:
    raw_data = f.read()
    data = [line.strip() for line in raw_data.split('\n')]
    mask = ''
    memory = {}

    for d in data:
        memory_address = None
        memory_int = None

        if d.split(' = ')[0] == 'mask':
            mask = d.split(' = ')[1].strip()
        else:
            memory_address = int(d.split(' = ')[0][4:-1])
            memory_int = int(d.split(' = ')[1])
            binary_str = bin(memory_address)
            formatted_binary = ''
            b_str_length = len(binary_str) - 2

            for i in range(0, 36-b_str_length):
                formatted_binary = formatted_binary + '0'
            formatted_binary = formatted_binary + binary_str[2:]

            # print(f"MASK: {mask} (length: {len(mask)})")
            # print(f"FORMATTED BINARY MEMORY ADDRESS: {formatted_binary} (length: {len(formatted_binary)})")

            masked_memory = ['0', 'b']
            for i in range(0, len(formatted_binary)):
                if mask[i] == 'X':
                    masked_memory.append(mask[i])
                elif mask[i] == '1':
                    masked_memory.append(mask[i])
                else:
                    masked_memory.append(formatted_binary[i])

            masked_str = ''.join(masked_memory)
            num_x = len(re.findall(r'X', masked_str))
            num_combos = 2 ** num_x
            print(f"BINARY MEMORY  ADDRESS WITH MASK APPLIED: {masked_str}")
            print(f"num_x: {num_x}, num_combos: {num_combos}")

            x_idx = []
            for i in range(0, len(masked_str)):
                if masked_str[i] == 'X':
                    x_idx.append(i)

            mask_perms = get_perms(len(x_idx))
            # print(len(mask_perms))
            # binary_memory_lst = []
            for perm in mask_perms:
                temp_str = masked_str[0:]
                for i in range(0, len(perm)):
                    temp_str = temp_str.replace('X', perm[i], 1)
                memory[int(temp_str, 2)] = memory_int

    print(sum(memory.values()))
