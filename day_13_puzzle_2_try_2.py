# Solution that can actually solve with the correct input

with open('day_13_puzzle_1_input.txt') as f:
    raw_data = f.read()
    raw_buses = list(raw_data.split('\n')[1].split(','))

    buses = []
    for i in range(0, len(raw_buses)):
        if raw_buses[i] == 'x':
            continue
        else:
            buses.append((i, int(raw_buses[i])))

    bus_1_time = buses[0][1]

    step = bus_1_time
    temp_time = bus_1_time
    for bus in buses[1:]:
        while (temp_time + bus[0]) % bus[1] != 0:
            temp_time += step
        step = step * bus[1]

    print(f"FINAL TIMESTAMP: {temp_time}")



