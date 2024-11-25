data = {
    1: [
        {
            "question": "Who discovered gravity?",
            "options": ["A) Isaac Newton", "B) Albert Einstein", "C) Galileo Galilei", "D) Nikola Tesla"],
            "correct_answer": "A"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["A) Earth", "B) Jupiter", "C) Mars", "D) Saturn"],
            "correct_answer": "B"
        },
        {
            "question": "What is the chemical symbol for sodium?",
            "options": ["A) Na", "B) K", "C) Cl", "D) Mg"],
            "correct_answer": "A"
        }
    ],
    2: [
        {
            "question": "Who is known as the father of modern physics?",
            "options": ["A) Isaac Newton", "B) Albert Einstein", "C) Marie Curie", "D) Nikola Tesla"],
            "correct_answer": "B"
        },
        {
            "question": "Which planet is closest to the Sun?",
            "options": ["A) Mercury", "B) Venus", "C) Earth", "D) Mars"],
            "correct_answer": "A"
        },
        {
            "question": "What is the chemical symbol for water?",
            "options": ["A) H2O", "B) O2", "C) CO2", "D) H2"],
            "correct_answer": "A"
        }
    ],
    3: [
        {
            "question": "What is the capital of Japan?",
            "options": ["A) Beijing", "B) Tokyo", "C) Seoul", "D) Bangkok"],
            "correct_answer": "B"
        },
        {
            "question": "Who invented the lightbulb?",
            "options": ["A) Nikola Tesla", "B) Thomas Edison", "C) Alexander Graham Bell", "D) Albert Einstein"],
            "correct_answer": "B"
        },
        {
            "question": "What is the symbol of the element Gold?",
            "options": ["A) Au", "B) Ag", "C) Pb", "D) Fe"],
            "correct_answer": "A"
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
