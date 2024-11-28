data = {
    1: [
        {
            "question": "What is the tallest mountain in the world?",
            "options": ["A) Mount Everest", "B) K2", "C) Kangchenjunga", "D) Mount Kilimanjaro"],
            "correct_answer": "A"
        },
        {
            "question": "Which animal is known as the 'King of the Jungle'?",
            "options": ["A) Elephant", "B) Tiger", "C) Lion", "D) Bear"],
            "correct_answer": "C"
        },
        {
            "question": "What is the chemical symbol for oxygen?",
            "options": ["A) O", "B) O2", "C) Ox", "D) O3"],
            "correct_answer": "A"
        }
    ],
    2: [
        {
            "question": "Which planet is known as the 'Red Planet'?",
            "options": ["A) Venus", "B) Earth", "C) Mars", "D) Jupiter"],
            "correct_answer": "C"
        },
        {
            "question": "Who invented the telephone?",
            "options": ["A) Nikola Tesla", "B) Thomas Edison", "C) Alexander Graham Bell", "D) Galileo Galilei"],
            "correct_answer": "C"
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"],
            "correct_answer": "D"
        }
    ],
    3: [
        {
            "question": "Who painted the Mona Lisa?",
            "options": ["A) Leonardo da Vinci", "B) Pablo Picasso", "C) Vincent van Gogh", "D) Claude Monet"],
            "correct_answer": "A"
        },
        {
            "question": "What is the capital city of France?",
            "options": ["A) Rome", "B) Berlin", "C) Paris", "D) Madrid"],
            "correct_answer": "C"
        },
        {
            "question": "What is the hardest natural substance on Earth?",
            "options": ["A) Gold", "B) Iron", "C) Diamond", "D) Platinum"],
            "correct_answer": "C"
        }
    ]
}

def display_question(question_data):
    print(f"\n{question_data['question']}")
    for option in question_data['options']:
        print(option)
    
    while True:
        answer = input("Enter your answer (A, B, C, D): ").upper()
        if answer in ['A', 'B', 'C', 'D']:
            return answer
        else:
            print("Invalid input. Please enter a valid option: A, B, C, or D.")

def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        print("Correct! Well done!")
        return True
    else:
        print(f"Incorrect. The correct answer is {correct_answer}.")
        return False

def conduct_quiz(questions):
    score = 0
    total_questions = len(questions)
    
    for question_data in questions:
        user_answer = display_question(question_data)
        if check_answer(user_answer, question_data["correct_answer"]):
            score += 1
    
    print(f"\nYour final score is {score} out of {total_questions}.")
    print(f"Your score percentage is {score / total_questions * 100:.2f}%")
    
    if score == total_questions:
        print("Excellent!")
    elif score > total_questions / 2:
        print("Good try!")
    else:
        print("Try again! You can do better next time.")

def choose_quiz_set():
    print("Select a quiz set:")
    print("1. Set 1")
    print("2. Set 2")
    print("3. Set 3")
    
    while True:
        try:
            selected_set = int(input("Enter the number of the quiz set (1, 2, or 3): "))
            if selected_set in [1, 2, 3]:
                return selected_set
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number (1, 2, or 3).")

def game():
    print("Welcome to the Basic Quiz Game!")
    
    selected_set = choose_quiz_set()
    questions = data[selected_set]
    
    conduct_quiz(questions)

if __name__ == "__main__":
    game()
