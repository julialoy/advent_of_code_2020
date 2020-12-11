with open('day_10_puzzle_1_input.txt') as f:
    raw_data = f.read()
    adapters = [int(line.strip()) for line in raw_data.split('\n')]
    adapters.append(0)
    sorted_adapters = sorted(adapters)
    my_device = 3 + max(sorted_adapters)
    sorted_adapters.append(my_device)
    differences = [sorted_adapters[i+1] - sorted_adapters[i] for i in range(0, len(sorted_adapters)-1)]

    three_jolt_diff = 0
    one_jolt_diff = 0
    for diff in differences:
        if diff == 1:
            one_jolt_diff += 1
        elif diff == 3:
            three_jolt_diff += 1
        else:
            print("Error")

    print(one_jolt_diff * three_jolt_diff)
