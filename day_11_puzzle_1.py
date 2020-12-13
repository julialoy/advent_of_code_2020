#########################
### Coord cheat sheet ###
#########################
# up = (x, y-1)     Up as relates to looking at the map
# down = (x, y+1)   Down as relates to looking at the map
# right = (x+1, y)
# left = (x-1, y)
# diag_up_left = (x-1, y-1)
# diag_up_right = (x+1, y-1)
# diag_down_left = (x-1, y+1)
# diag_down_right = (x+1, y+1)


def change_seats(map, seat_changes):
    new_map = [[] for _ in range(0, len(map))]

    for y in range(0, len(map)):
        for x in range(0, len(map[y])):
            current_seat = map[y][x]
            if (x, y) in seat_changes:
                if current_seat == '#':
                    current_seat = 'L'
                elif current_seat == 'L':
                    current_seat = '#'
            new_map[y].append(current_seat)
    return new_map


def check_up(x, y, map):
    if map[y - 1][x] == '#':
        return True
    return False


def check_down(x, y, map):
    if map[y+1][x] == '#':
        return True
    return False


def check_right(x, y, map):
    if map[y][x+1] == '#':
        return True
    return False


def check_left(x, y, map):
    if map[y][x-1] == '#':
        return True
    return False


def check_diag_up_left(x, y, map):
    if map[y-1][x-1] == '#':
        return True
    return False


def check_diag_up_right(x, y, map):
    if map[y-1][x+1] == '#':
        return True
    return False


def check_diag_down_left(x, y, map):
    if map[y+1][x-1] == '#':
        return True
    return False


def check_diag_down_right(x, y, map):
    if map[y+1][x+1] == '#':
        return True
    return False


def return_num_occ_seats(bool_list):
    num_true = 0
    for bool in bool_list:
        if bool:
            num_true += 1
    return num_true


def check_seat_state(map, changes):
    if not changes:
        return map

    new_seat_state = []
    changes = False

    for y in range(0, len(map)):
        for x in range(0, len(map[y])):
            current_seat = map[y][x]
            num_adj_occ = 0

            # Skip if "Seat" is floor
            if current_seat == '.':
                continue

            # If seat is in first row but not a corner
            if y == 0 and x != 0 and x != len(map[0])-1:
                num_adj_occ += return_num_occ_seats([check_left(x, y, map),
                                                     check_right(x, y, map),
                                                     check_down(x, y, map),
                                                     check_diag_down_left(x, y, map),
                                                     check_diag_down_right(x, y, map)])
            # If seat is in first row and top left corner
            elif y == 0 and x == 0:
                num_adj_occ += return_num_occ_seats([check_right(x, y, map),
                                                     check_down(x, y, map),
                                                     check_diag_down_right(x, y, map)])
            # If seat is in first row and top right corner
            elif y == 0 and x == len(map[0]) - 1:
                num_adj_occ += return_num_occ_seats([check_left(x, y, map),
                                                     check_down(x, y, map),
                                                     check_diag_down_left(x, y, map)])
            # If seat is on left bottom corner
            elif y == len(map) - 1 and x == 0:
                num_adj_occ += return_num_occ_seats([check_up(x, y, map),
                                                     check_diag_up_right(x, y, map),
                                                     check_right(x, y, map)])
            # If seat is in right bottom corner
            elif y == len(map) - 1 and x == len(map[y]) - 1:
                num_adj_occ += return_num_occ_seats([check_up(x, y, map),
                                                     check_left(x, y, map),
                                                     check_diag_up_left(x, y, map)])
            # If seat is on left edge but not a corner
            elif x == 0:
                num_adj_occ += return_num_occ_seats([check_up(x, y, map),
                                                     check_right(x, y, map),
                                                     check_diag_up_right(x, y, map),
                                                     check_diag_down_right(x, y, map),
                                                     check_down(x, y, map)])
            # If seat is on right edge but not a corner
            elif x == len(map[y]) - 1:
                num_adj_occ += return_num_occ_seats([check_up(x, y, map),
                                                     check_diag_up_left(x, y, map),
                                                     check_left(x, y, map),
                                                     check_diag_down_left(x, y, map),
                                                     check_down(x, y, map)])
            # If seat is on bottom row but not a corner
            elif y == len(map) - 1:
                num_adj_occ += return_num_occ_seats([check_up(x, y, map),
                                                     check_left(x, y, map),
                                                     check_diag_up_left(x, y, map),
                                                     check_diag_up_right(x, y, map),
                                                     check_right(x, y, map)])
            # If seat is any other seat
            else:
                num_adj_occ += return_num_occ_seats([check_up(x, y, map),
                                                     check_down(x, y, map),
                                                     check_diag_up_left(x, y, map),
                                                     check_diag_up_right(x, y, map),
                                                     check_left(x, y, map),
                                                     check_right(x, y, map),
                                                     check_diag_down_left(x, y, map),
                                                     check_diag_down_right(x, y, map)])

            # Seat occupied
            # Check if seat becomes empty
            if current_seat == '#':
                if num_adj_occ >= 4:
                    changes = True
                    new_seat_state.append((x, y))
            # Seat empty
            # Check if seat becomes occupied
            elif current_seat == 'L':
                if num_adj_occ == 0:
                    changes = True
                    new_seat_state.append((x, y))

    map = change_seats(map, new_seat_state)

    return check_seat_state(map, changes)


def total_seats_occ(map):
    total = 0
    for y in range(0, len(map)):
        for x in range(0, len(map[y])):
            if map[y][x] == '#':
                total += 1
    return total


with open('day_11_puzzle_1_input.txt') as f:
    raw_data = f.read()
    map = [[char.strip() for char in list(line)] for line in raw_data.split('\n')]
    map_1 = check_seat_state(map, True)

    print(total_seats_occ(map_1))

