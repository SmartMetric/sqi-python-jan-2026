q1 = {
    "question": "What is 2 + 2?",
    "options": {"a": "3", "b": "4", "c": "5", "d": "6"},
}

q2 = {
    "question": "What color is the sky on a clear day?",
    "options": {"a": "Red", "b": "Blue", "c": "Green", "d": "Yellow"},
}

q3 = {
    "question": "How many legs does a spider have?",
    "options": {"a": "6", "b": "7", "c": "8", "d": "9"},
}

q4 = {
    "question": "What sound does a cow make?",
    "options": {"a": "Meow", "b": "Bark", "c": "Moo", "d": "Quack"},
}

q5 = {
    "question": "What is the opposite of 'hot'?",
    "options": {"a": "Warm", "b": "Cold", "c": "Cool", "d": "Boiling"},
}

cbt_exam_questions = [q1, q2, q3, q4, q5]


answer1 = "b"
answer2 = "b"
answer3 = "c"
answer4 = "c"
answer5 = "b"

cbt_exam_answers = [answer1, answer2, answer3, answer4, answer5]


def collect_answers():
    answers = []

    for question_number, exam_question in enumerate(cbt_exam_questions, start=1):
        print(f"{question_number}. {exam_question['question']}")
        for option_letter, option_text in exam_question["options"].items():
            print(f"{option_letter}) {option_text}")
        print()

        user_input = input("Enter your answer (a, b, c, or d): ").strip().lower()
        answers.append(user_input)
        print()

    return answers


def compare_answers(user_answers, correct_answers):
    score = 0
    for user_answer, correct_answer in zip(user_answers, correct_answers):
        if user_answer == correct_answer:
            score += 1
    return score


user_answers = collect_answers()
score = compare_answers(user_answers, cbt_exam_answers)

print(f"You scored {score} out of {len(cbt_exam_answers)}")
