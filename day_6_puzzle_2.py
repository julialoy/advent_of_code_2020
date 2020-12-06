with open('day_6_puzzle_1_input.txt') as f:
    raw_data = f.read()
    question_data = [[individual.strip() for individual in answers.split('\n')] for answers in raw_data.split('\n\n')]
    total = 0

    for group in question_data:
        answered = 0
        if len(group) == 1:
            answered = len(group[0])
        else:
            num_in_group = len(group)
            question_dict = {}
            for question_set in group:
                questions = list(question_set)
                for question in questions:
                    if question in question_dict:
                        question_dict[question] += 1
                    else:
                        question_dict[question] = 1

            for k, v in question_dict.items():
                if v == num_in_group:
                    answered += 1
        total += answered

    print(total)
