def contains_shiny_gold(bag_dict, bags, bag):
    for k,v in bag_dict.items():
        if not isinstance(v, dict):
            continue
        if bag in v.keys():
            bags.append(k)
            contains_shiny_gold(bag_dict, bags, k)
    return bags


def get_final_bags(bag_list):
    final = []
    for bg in bag_list:
        if bg not in final:
            final.append(bg)
    return final


sample_dict = {'light red': {'bright white': 1, 'muted yellow': 2},
               'dark orange': {'bright white': 3, 'muted yellow': 4},
               'bright white': {'shiny gold': 1},
               'muted yellow': {'shiny gold': 2, 'faded blue': 9},
               'shiny gold': {'dark olive': 1, 'vibrant plum': 2},
               'dark olive': {'faded blue': 3, 'dotted black': 4},
               'vibrant plum': {'faded blue': 5, 'dotted black': 6},
               'faded blue': 0,
               'dotted black': 0}

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

    some_bags_list = []
    some_bags = contains_shiny_gold(rules, some_bags_list, 'shiny gold')
    final_bags = get_final_bags(some_bags)
    print(len(final_bags))
