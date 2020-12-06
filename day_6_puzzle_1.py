with open('day_6_puzzle_1_input.txt') as f:
    raw_data = f.read()
    question_data = [[individual.strip() for individual in answers.split('\n')] for answers in raw_data.split('\n\n')]
    total = 0
    for group in question_data:
        unique_questions = []
        for question_set in group:
            questions = list(question_set)
            for question in questions:
                if question not in unique_questions:
                    unique_questions.append(question)
        total += len(unique_questions)

    print(total)


