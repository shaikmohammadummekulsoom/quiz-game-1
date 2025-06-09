import time

# Define quiz questions
quiz = [
    {
        "question": "What is the capital of France?",
        "options": ["A. London", "B. Paris", "C. Berlin", "D. Rome"],
        "answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Jupiter", "C. Mars", "D. Saturn"],
        "answer": "C"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["A. William Wordsworth", "B. William Shakespeare", "C. Charles Dickens", "D. Jane Austen"],
        "answer": "B"
    },
    {
        "question": "Which is the smallest prime number?",
        "options": ["A. 0", "B. 1", "C. 2", "D. 3"],
        "answer": "C"
    }
]

# Function to run the quiz
def run_quiz():
    score = 0
    answers_given = []

    print("\n📘 Welcome to the Quiz Game!\n")
    time.sleep(1)

    for index, q in enumerate(quiz):
        print(f"\nQ{index + 1}: {q['question']}")
        for option in q['options']:
            print(option)

        start_time = time.time()
        user_answer = input("Your answer (A/B/C/D): ").strip().upper()
        elapsed_time = time.time() - start_time

        if user_answer == q['answer']:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Incorrect. The correct answer was {q['answer']}.")

        answers_given.append((q['question'], user_answer, q['answer'], elapsed_time))

    # Show results
    print("\n🎉 Quiz Completed!")
    print(f"Your Final Score: {score}/{len(quiz)}\n")

    print("📋 Answer Review:")
    for i, (question, given, correct, time_taken) in enumerate(answers_given, 1):
        status = "✅" if given == correct else "❌"
        print(f"{i}. {question}")
        print(f"   Your Answer: {given} | Correct: {correct} | Time: {round(time_taken, 2)}s | {status}")

# Run the program
if __name__ == "__main__":
    run_quiz()
