import re

with open('day_2_puzzle_1_input.txt') as f:
    raw_data = f.read().split('\n')
    rules = [(line.split(' ')[0].strip(), line.split(' ')[1].split(':')[0].strip()) for line in raw_data]
    passwords = [line.split(':')[1].strip() for line in raw_data]
    num_valid_passwords = 0

    for i in range(0, len(rules)):
        min_num = int(rules[i][0].split('-')[0])
        max_num = int(rules[i][0].split('-')[1])
        req_char = rules[i][1]
        valid_pass = False

        if req_char in passwords[i]:
            char_matches = re.findall(req_char, passwords[i])
            if min_num <= len(char_matches) <= max_num:
                valid_pass = True
        elif req_char not in passwords[1] and min_num != 0:
            valid_pass = False

        if valid_pass:
            num_valid_passwords += 1

    print(f"There are {num_valid_passwords} valid passwords.")


