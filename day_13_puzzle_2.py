# Horribly inefficient solution that may or may not work on actual input but works on short examples
with open('day_13_puzzle_1_input.txt') as f:
    raw_data = f.read()
    raw_buses = list(raw_data.split('\n')[1].split(','))

    buses = []
    largest_bus = 0
    largest_bus_idx = 0
    for i in range(0, len(raw_buses)):
        if raw_buses[i] == 'x':
            continue
        else:
            buses.append((i, int(raw_buses[i])))
            if int(raw_buses[i]) > largest_bus:
                largest_bus = int(raw_buses[i])
                largest_bus_idx = i

    bus_1_time = buses[0][1]
    timestamp = None
    start_time = 0
    count = 0
    while start_time < largest_bus:
        count += 1
        start_time = count * bus_1_time

    largest_remainder = 0
    temp_time = start_time
    while not timestamp:
        remainders = []
        time_valid = True
        largest_remainder = 0
        for bus in buses[1:]:
            remainders.append((temp_time + bus[0]) % bus[1])

        for remainder in remainders:
            if remainder != 0:
                time_valid = False

        if time_valid:
            timestamp = temp_time
            break
        else:
            for bus in buses[1:]:
                r = temp_time % bus[1]
                if r > largest_remainder:
                    largest_remainder = r

        if largest_remainder > count:
            count = largest_remainder
        else:
            count += 1

        temp_time = count * bus_1_time

    print(f"FINAL TIMESTAMP: {timestamp}")
