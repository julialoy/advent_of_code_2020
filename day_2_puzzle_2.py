import re

with open('day_2_puzzle_1_input.txt') as f:
    raw_data = f.read().split('\n')
    rules = [(line.split(' ')[0], line.split(' ')[1].split(':')[0]) for line in raw_data]
    passwords = [line.split(':')[1] for line in raw_data]
    num_valid_passwords = 0

    for i in range(0, len(rules)):
        valid_pass = False
        pos_1 = int(rules[i][0].split('-')[0])
        pos_2 = int(rules[i][0].split('-')[1])
        req_char = rules[i][1]
        char_pos_1 = passwords[i][pos_1:pos_1+1]
        char_pos_2 = passwords[i][pos_2:pos_2+1]

        if char_pos_1 is req_char and char_pos_2 is not req_char:
            valid_pass = True
            print(f"{rules[i]}, {passwords[i]} is valid: position 1 ({pos_1}) character is {char_pos_1}, "
                  f"position 2 ({pos_2}) character is {char_pos_2}")
        elif char_pos_1 is not req_char and char_pos_2 is req_char:
            valid_pass = True
            print(f"{rules[i]}, {passwords[i]} is valid: position 1 ({pos_1}) character is {char_pos_1}, "
                  f"position 2 ({pos_2}) character is {char_pos_2}")
        else:
            valid_pass = False

        if valid_pass:
            num_valid_passwords += 1

    print(f"There are {num_valid_passwords} valid passwords.")


