with open('day_1_puzzle_1_input.txt') as f:
    raw_expense_report = f.read()
    expense_array = [int(num) for num in raw_expense_report.split('\n')]
    for i in range(0, len(expense_array)-1):
        for j in range(i+1, len(expense_array)):
            for z in range(j+1, len(expense_array)):
                result = expense_array[i] + expense_array[j] + expense_array[z]
                if result == 2020:
                    product = expense_array[i] * expense_array[j] * expense_array[z]
                    print(product)
