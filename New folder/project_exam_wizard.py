q1 = {
    "question": "Explain the meaning of the legal term 'stare decisis'.",
    "keywords": {
        "precedent": 3,
        "binding": 2,
        "previous decisions": 2,
        "courts": 1,
        "similar cases": 2,
        "consistency": 2,
        "certainty": 2
    }
}

q2 = {
    "question": "Explain the legal term 'mens rea'.",
    "keywords": {
        "guilty mind": 3,
        "mental element": 2,
        "intention": 2,
        "knowledge": 1,
        "recklessness": 1,
        "negligence": 1,
        "criminal liability": 2
    }
}

q3 = {
    "question": "Explain the meaning of 'actus reus'.",
    "keywords": {
        "guilty act": 3,
        "physical element": 2,
        "conduct": 2,
        "omission": 1,
        "criminal offence": 2,
        "legal duty": 1
    }
}

q4 = {
    "question": "Explain the legal maxim 'ubi jus ibi remedium'.",
    "keywords": {
        "where there is a right": 3,
        "remedy": 2,
        "legal wrong": 1,
        "enforcement": 2,
        "court": 1,
        "redress": 1
    }
}

q5 = {
    "question": "Explain the legal term 'res ipsa loquitur'.",
    "keywords": {
        "thing speaks for itself": 3,
        "negligence": 2,
        "burden of proof": 2,
        "accident": 1,
        "exclusive control": 2,
        "defendant": 1
    }
}

theory_exam_questions = [q1, q2, q3, q4, q5]


def collect_answers():
    answers = []

    for question_number, exam_question in enumerate(theory_exam_questions, start=1):
        print(f"{question_number}. {exam_question['question']}")
        user_input = input("Enter your answer: ").strip().lower()
        answers.append(user_input)
        print()

    return answers


def score_answers(user_answers, exam_questions):
    total_score = 0
    max_score = 0

    for  user_answer, exam_question in zip(user_answers, exam_questions):
        keywords = exam_question["keywords"]

        max_score += sum(keywords.values())

       
        for keyword, allocated_marks in keywords.items():

            if keyword.lower() in user_answer:
                total_score += allocated_marks 

    return total_score, max_score


user_answers = collect_answers()
total_score, max_score = score_answers(user_answers, theory_exam_questions)

print(f"You scored {total_score} out of {max_score}")
