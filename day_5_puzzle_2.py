with open('day_5_puzzle_1_input.txt') as f:
    raw_data = f.read()
    raw_seats = [seat.strip() for seat in raw_data.split('\n')]
    plane_rows = [i for i in range(0, 128)]
    plane_cols = [i for i in range(0, 8)]
    seat_nums = []

    for seat in raw_seats:
        # print(f"SEAT: {seat}")
        chars = list(seat)
        seat_row = plane_rows
        seat_col = plane_cols
        for char in chars:
            # print(f"CHAR: {char}")
            if char == 'F':
                plane_half = int(len(seat_row) / 2)
                # print(f"PLANE_HALF: {plane_half}")
                seat_row = seat_row[:plane_half]
                # print(f"SEAT_ROW: {seat_row}")
            elif char == 'B':
                plane_half = int(len(seat_row) / 2)
                seat_row = seat_row[plane_half:]
            elif char == 'L':
                col_half = int(len(seat_col) / 2)
                seat_col = seat_col[:col_half]
            elif char == 'R':
                col_half = int(len(seat_col) / 2)
                seat_col = seat_col[col_half:]
        seat_id = seat_row[0] * 8 + seat_col[0]
        seat_nums.append(seat_id)

    seat_ids = sorted(seat_nums)
    possible_seats = []

    for x in range(1, len(seat_ids)-1):
        if seat_ids[x+1] - seat_ids[x] != 1:
            possible_seats.append(seat_ids[x])
            possible_seats.append(seat_ids[x+1])

    my_seat = possible_seats[0] + 1
    print(my_seat)
