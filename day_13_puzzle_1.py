with open('day_13_puzzle_1_input.txt') as f:
    raw_data = f.read()
    earliest = int(raw_data.split('\n')[0].strip())
    buses = list(raw_data.split('\n')[1].split(','))
    closest = []

    for bus in buses:
        if bus == 'x':
            continue

        bus_id = int(bus)
        i = 0
        while i < earliest:
            if bus_id * i >= earliest:
                closest.append((bus_id, bus_id * i))
            i += 1

    final_time = closest[0][1] - earliest
    earliest_bus_id = 0
    for time in closest[1:]:
        if time[1] - earliest < final_time:
            final_time = time[1] - earliest
            earliest_bus_id = time[0]

    print(earliest_bus_id * final_time)
