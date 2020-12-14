def change_direction(curr_direction, rotation_direction, rotation_degree):
    new_direction = None
    compass = ['N', 'E', 'S', 'W']
    curr_idx = compass.index(curr_direction)
    move_by = int(rotation_degree / 90)
    new_idx = 0

    if rotation_direction == 'R':
        new_idx = curr_idx + move_by
    elif rotation_direction == 'L':
        new_idx = curr_idx - move_by

    if 0 <= new_idx < len(compass):
        new_direction = compass[new_idx]
    elif new_idx >= len(compass):
        new_idx = new_idx - len(compass)
        new_direction = compass[new_idx]
    elif 0 > new_idx < -4:
        new_direction = compass[new_idx]
    elif 0 > new_idx > -4:
        new_idx = new_idx + len(compass)
        new_direction = compass[new_idx]

    return new_direction


with open('day_12_puzzle_1_input.txt') as f:
    raw_data = f.read()
    coord_lst = [line.strip() for line in raw_data.split('\n')]

    n_s_total = 0
    e_w_total = 0

    facing = 'E'
    for coord in coord_lst:
        d = coord[:1]
        n = int(coord[1:])
        if d == 'N':
            n_s_total += n
        elif d == 'S':
            n_s_total = n_s_total - n
        elif d == 'E':
            e_w_total += n
        elif d == 'W':
            e_w_total = e_w_total - n
        elif d == 'L' or d == 'R':
            facing = change_direction(facing, d, n)
        elif d == 'F':
            if facing == 'N':
                n_s_total += n
            elif facing == 'S':
                n_s_total = n_s_total - n
            elif facing == 'E':
                e_w_total += n
            elif facing == 'W':
                e_w_total = e_w_total - n

    manhattan_distance = abs(n_s_total) + abs(e_w_total)
    print(manhattan_distance)

