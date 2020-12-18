with open('day_14_puzzle_1_input.txt') as f:
    raw_data = f.read()
    data = [line.strip() for line in raw_data.split('\n')]
    mask = ''
    memory = {}

    for d in data:
        memory_address = None
        memory_int = None

        if d.split(' = ')[0] == 'mask':
            mask = d.split(' = ')[1].strip()
        else:
            memory_address = int(d.split(' = ')[0][4:-1])
            memory_int = int(d.split(' = ')[1])
            binary_str = bin(memory_int)
            formatted_binary = ''
            b_str_length = len(binary_str) - 2

            for i in range(0, 36-b_str_length):
                formatted_binary = formatted_binary + '0'
            formatted_binary = formatted_binary + binary_str[2:]

            masked_binary = '0b'
            for i in range(0, len(mask)):
                if mask[i] != 'X':
                    masked_binary = masked_binary + mask[i]
                else:
                    masked_binary = masked_binary + formatted_binary[i]

            memory[memory_address] = int(masked_binary, 2)

    print(sum(memory.values()))
