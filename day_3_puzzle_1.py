with open('day_3_puzzle_1_input.txt') as f:
    raw_data = f.read()
    map_array = [[square.strip() for square in list(line)] for line in raw_data.split('\n')]
    map_length = len(map_array) - 1
    map_width = len(map_array[map_length]) - 1
    num_trees = 0
    curr_y = 0
    curr_x = 0

    while curr_y < map_length:
        curr_y += 1
        if (curr_x + 3) > map_width:
            curr_x = (curr_x + 3) - map_width - 1
        else:
            curr_x += 3
        if map_array[curr_y][curr_x] == '#':
            num_trees += 1

    print(num_trees)
