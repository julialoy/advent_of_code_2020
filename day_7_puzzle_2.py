def find_bag_count(input_dict, bg_lst, count):
    if len(bg_lst) == 0:
        return count
    if not isinstance(input_dict[bg_lst[0][0]], dict):
        count.append(0)
        bg_lst = bg_lst[1:]
        return find_bag_count(input_dict, bg_lst, count)
    else:
        inside_count = 0
        for k,v in input_dict[bg_lst[0][0]].items():
            inside_count += v * bg_lst[0][1]
            bg_lst.append((k, bg_lst[0][1] * v))
        count.append(inside_count)
        bg_lst = bg_lst[1:]
        return find_bag_count(input_dict, bg_lst, count)


sample_dict = {'light red': {'bright white': 1, 'muted yellow': 2},
               'dark orange': {'bright white': 3, 'muted yellow': 4},
               'bright white': {'shiny gold': 1},
               'muted yellow': {'shiny gold': 2, 'faded blue': 9},
               'shiny gold': {'dark olive': 1, 'vibrant plum': 2},
               'dark olive': {'faded blue': 3, 'dotted black': 4},
               'vibrant plum': {'faded blue': 5, 'dotted black': 6},
               'faded blue': 0,
               'dotted black': 0}

sample_dict_2 = {'shiny gold': {'dark red': 2},
                 'dark red': {'dark orange': 2},
                 'dark orange': {'dark yellow': 2},
                 'dark yellow': {'dark green': 2},
                 'dark green': {'dark blue': 2},
                 'dark blue': {'dark violet': 2},
                 'dark violet': 0}

with open('day_7_puzzle_1_input.txt') as f:
    raw_data = f.read()
    raw_data_formatted = raw_data.replace('.', '').replace(' bags', '').replace(' bag', '')
    lines = [[bags for bags in line.split(' contain ')] for line in raw_data_formatted.split('\n')]
    rules = {}
    for line in lines:
        outer_bag = line[0]
        inner_bags = line[1].rstrip('.').split(', ')
        rules[outer_bag] = {}
        for bag in inner_bags:
            if bag == 'no other':
                rules[outer_bag] = 0
                continue
            else:
                first_space = bag.find(' ')
                num_bags = bag[:first_space]
                num_bags = int(num_bags)
                color_bags = bag[first_space + 1:]
                rules[outer_bag][color_bags] = num_bags

    print(sum(find_bag_count(rules, [('shiny gold', 1)], [])))
