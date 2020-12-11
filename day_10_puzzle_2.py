with open('day_10_puzzle_1_input.txt') as f:
    raw_data = f.read()
    adapters = [int(line.strip()) for line in raw_data.split('\n')]
    adapters.append(0)
    sorted_adapters = sorted(adapters)
    differences = [sorted_adapters[i+1] - sorted_adapters[i] for i in range(0, len(sorted_adapters)-1)]

    combinations = 1
    while len(differences) > 0:
        try:
            split_index = differences.index(3)
            current_sublist, differences = differences[:split_index], differences[split_index+1:]
        except ValueError:
            current_sublist = differences
            differences = []

        for num in current_sublist:
            if num != 1:
                print(f"{num}: something went wrong")

        if len(current_sublist) == 0:
            continue
        else:
            sub_combos = 0
            for i in range(0, len(current_sublist)):
                if i == 0:
                    sub_combos += 1
                elif i == 1:
                    sub_combos += 1
                else:
                    sub_combos += i
            combinations = combinations * sub_combos

    print(combinations)
