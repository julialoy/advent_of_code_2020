num_array = [8, 0, 17, 4, 1, 12]

while len(num_array) < 2021:
    last_num = num_array[-1]
    if last_num in num_array[:-1]:
        for i in range(len(num_array)-2, -1, -1):
            if num_array[i] == last_num:
                num_array.append(len(num_array) - (i+1))
                break
    else:
        num_array.append(0)

    print(len(num_array))

    if len(num_array) == 2020:
        break

print(num_array[-1])
