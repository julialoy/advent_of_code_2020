def change_direction(curr_n_s, curr_e_w, rotation_direction, rotation_degree):
    new_n_s = curr_n_s
    new_e_w = curr_e_w

    if rotation_direction == 'L':
        move_by = int(-(rotation_degree / 90))
        while move_by < 0:
            temp_n_s = new_n_s
            temp_e_w = new_e_w
            new_n_s = temp_e_w
            new_e_w = -temp_n_s
            move_by += 1
    elif rotation_direction == 'R':
        move_by = int(rotation_degree / 90)
        while move_by > 0:
            temp_n_s = new_n_s
            temp_e_w = new_e_w
            new_n_s = -temp_e_w
            new_e_w = temp_n_s
            move_by = move_by - 1

    return new_n_s, new_e_w


with open('day_12_puzzle_1_input.txt') as f:
    raw_data = f.read()
    coord_lst = [line.strip() for line in raw_data.split('\n')]

    waypoint_n_s = 1
    waypoint_e_w = 10

    ship_n_s_total = 0
    ship_e_w_total = 0

    for coord in coord_lst:
        d = coord[:1]
        n = int(coord[1:])
        if d == 'N':
            waypoint_n_s += n
        elif d == 'S':
            waypoint_n_s = waypoint_n_s - n
        elif d == 'E':
            waypoint_e_w += n
        elif d == 'W':
            waypoint_e_w = waypoint_e_w - n
        elif d == 'L' or d == 'R':
            waypoint_n_s, waypoint_e_w = change_direction(waypoint_n_s, waypoint_e_w, d, n)
        elif d == 'F':
            ship_n_s_total += waypoint_n_s * n
            ship_e_w_total += waypoint_e_w * n

    manhattan_distance = abs(ship_n_s_total) + abs(ship_e_w_total)
    print(manhattan_distance)

