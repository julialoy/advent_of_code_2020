def run_instructions(instructions):
    prev_visited_idxs = []
    accumulator = 0
    i = 0
    while i not in prev_visited_idxs and i < len(instructions):
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
            return prev_visited_idxs, None, i

        i = next_instruction
    return prev_visited_idxs, accumulator, i


with open('day_8_puzzle_1_input.txt') as f:
    raw_data = f.read()
    instrucs = [(line.split(' ')[0].strip(), int(line.split(' ')[1].strip())) for line in raw_data.split('\n')]
    prev_idxs, acc_value, final_index = run_instructions(instrucs)

    correct_fix_found = False
    for idx in prev_idxs:
        if instrucs[idx][0] == 'jmp':
            try:
                new_instruction = ('noc', instrucs[idx][1])
                replacement_instructions = [new_instruction if j==idx else instrucs[j]
                                            for j in range(0, len(instrucs)-1)]
                new_prev_idx, new_acc_value, new_final_index = run_instructions(replacement_instructions)
            except IndexError:
                print(f"Not correct fix")
            else:
                if new_acc_value is None:
                    continue
                else:
                    print(f"Correct fix")
                    correct_fix_found = True
                    print(f"New accumulator value: {new_acc_value}")
                    break

    if not correct_fix_found:
        for idx in prev_idxs:
            if instrucs[idx][0] == 'noc':
                try:
                    new_instruction_2 = ('jmp', instrucs[idx][1])
                    replacement_instructions_2 = [new_instruction_2 if x==idx else instrucs[x]
                                                  for x in range(0, len(instrucs) - 1)]
                    new_prev_idx_2, new_acc_value_2, new_final_index_2 = run_instructions(replacement_instructions_2)
                except IndexError:
                    print(f"Not correct fix")
                else:
                    if new_acc_value_2 is None:
                        continue
                    else:
                        correct_fix_found = True
                        print(f"New accumulator value: {new_acc_value_2}")
                        break

    if not correct_fix_found:
        print(f"Still no fix found. Something terrible happened.")

