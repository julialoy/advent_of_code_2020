with open('day_8_puzzle_1_input.txt') as f:
    raw_data = f.read()
    instructions = [(line.split(' ')[0].strip(), int(line.split(' ')[1].strip())) for line in raw_data.split('\n')]

    prev_visited_idxs = []
    accumulator = 0
    i = 0
    while i not in prev_visited_idxs:
        next_instruction = i+1
        prev_visited_idxs.append(i)

        if instructions[i][0] == 'nop':
            i = next_instruction
            continue
        elif instructions[i][0] == 'acc':
            accumulator += instructions[i][1]
        elif instructions[i][0] == 'jmp':
            next_instruction = i+instructions[i][1]

        if next_instruction in prev_visited_idxs:
            print(f"Accumulator is {accumulator}")
            break

        i = next_instruction
