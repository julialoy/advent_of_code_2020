import re

with open('day_4_puzzle_1_input.txt') as f:
    raw_data = f.read()
    passports = [[(line.split(':')[0].strip(), line.split(':')[1].strip()) for line in re.split(r'\s', passport)]
                 for passport in raw_data.split('\n\n')]
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    valid_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    num_valid_passports = 0
    valid_passports = []

    for passport in passports:
        all_fields_present = True
        all_fields_valid = True
        present_fields = []
        field_data = {}

        for k, v in passport:
            for field in required_fields:
                if field == k:
                    present_fields.append(field)
                    field_data[k] = v

        for field in required_fields:
            if field not in present_fields:
                all_fields_present = False

        if all_fields_present:
            while all_fields_valid:
                if int(field_data['byr']) < 1920 or int(field_data['byr']) > 2002:
                    all_fields_valid = False
                    break

                if int(field_data['iyr']) < 2010 or int(field_data['iyr']) > 2020:
                    all_fields_valid = False
                    break

                if int(field_data['eyr']) < 2020 or int(field_data['eyr']) > 2030:
                    all_fields_valid = False
                    break

                if field_data['hgt'][-2:] != 'cm' and field_data['hgt'][-2:] != 'in':
                    all_fields_valid = False
                    break
                elif field_data['hgt'][-2:] == 'cm':
                    hgt_data = int(field_data['hgt'][:-2])
                    if hgt_data < 150 or hgt_data > 193:
                        all_fields_valid = False
                        break
                elif field_data['hgt'][-2:] == 'in':
                    hgt_data = int(field_data['hgt'][:-2])
                    if hgt_data < 59 or hgt_data > 76:
                        all_fields_valid = False
                        break

                if field_data['hcl'][0:1] != '#':
                    all_fields_valid = False
                    break
                elif field_data['hcl'][0:1] == '#':
                    hex_num = field_data['hcl'][1:]
                    if len(hex_num) != 6:
                        all_fields_valid = False
                        break
                    elif len(re.findall(r'[^a-f0-9]', hex_num)) != 0:
                        all_fields_valid = False
                        break

                if field_data['ecl'] not in valid_ecl:
                    all_fields_valid = False
                    break

                if len(field_data['pid']) != 9:
                    all_fields_valid = False
                    break
                else:
                    try:
                        int(field_data['pid'])
                    except ValueError:
                        all_fields_valid = False
                break

            if all_fields_valid:
                num_valid_passports += 1

    print(f"{num_valid_passports} valid passports")
