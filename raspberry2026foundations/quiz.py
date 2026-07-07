# Quiz

score = 0

questions = [
    {
        "question": "1. What is the capital of Australia?",
        "options": ["A. Perth", "B. Sydney", "C. Melbourne", "D. Canberra"],
        "answer": "D"
    },
    {
        "question": "2. What is the capital of Belgium?",
        "options": ["A. Brussels", "B. Ghent", "C. Bruges", "D. Antwerp"],
        "answer": "A"
    },
    {
        "question": "3. What is the capital of Canada?",
        "options": ["A. Calgary", "B. Edmonton", "C. Ottawa", "D. Toronto"],
        "answer": "C"
    }
]

print("=== Welcome to My Quiz ===\n")

for q in questions:
    print(q["question"])

    for option in q["options"]:
        print(option)

    response = input("Enter your answer (A, B, C, or D): ").strip().upper()

    if response == q["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Incorrect... The correct answer was {q['answer']}.\n")

    print("=" * 40)

print(f"Your final score is {score}/{len(questions)}")