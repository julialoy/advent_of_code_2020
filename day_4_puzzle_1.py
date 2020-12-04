import re

with open('day_4_puzzle_1_input.txt') as f:
    raw_data = f.read()
    passports = [[(line.split(':')[0].strip(), line.split(':')[1].strip()) for line in re.split(r'\s', passport)]
                 for passport in raw_data.split('\n\n')]
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    num_valid_passports = 0

    for passport in passports:
        all_fields_present = True
        present_fields = []

        for k, v in passport:
            for field in required_fields:
                if field == k:
                    present_fields.append(field)

        for field in required_fields:
            if field not in present_fields:
                all_fields_present = False

        if all_fields_present:
            num_valid_passports += 1

    print(f"{num_valid_passports} valid passports")
