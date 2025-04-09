quiz_questions = {
    "What is the formula for cubic parabola's?": ["y = ax^2+bx+c", "y = ax^3+bx^2+cx+d", "r^2 = (x-a)^2 + (y+b)^2", "y = mx + c"],
    "Differentiate f(x) = 2x^2+4x+6 	If x = 2": ["f'(2) = 6", "f'(2) = 5", "f'(2) = 12", "f'(2) = 40"],
    "Find the gradient of f(x) = 4x^2+2x+7	When y = 6": ["f'(x) = 8x - 4", "f'(x) = 4x + 8", "f'(x) = 8x + 8", "f'(x) = 4x - 4"],
    "If the gradient of a function is f'(x) = 4x + 2, find f(x) if it passes through (2,4)": ["f(x) = 4x^2 +2x + 8", "f(x) = 2x^2 + 4x + 2", "f(x) = 4x^2 + 4x + 8", "f(x) = 2x^2 + 2x - 8"],
    "What is the coordinate of the turning point of f(x) = 4x^2 + 2x + 5": ["(0.25, -4.75)","(0.25, 4.75)" ,"(-0.25 , 4.75)", "(4.75 , -0.25)"]
}

correct_answers = {
    "What is the formula for cubic parabola's?": "y = ax^3+bx^2+cx+d",
    "Differentiate f(x) = 2x^2+4x+6 	If x = 2": "f'(2) = 12",
    "Find the gradient of f(x) = 4x^2+2x+7	When y = 6": "f'(x) = 8x + 8",
    "If the gradient of a function is f'(x) = 4x + 2, find f(x) if it passes through (2,4)": "f(x) = 2x^2 + 2x - 8",
    "What is the coordinate of the turning point of f(x) = 4x^2 + 2x + 5": "(-0.25 , 4.75)"
}

MAX_AGE = 18
MIN_AGE = 12

def Play_Quiz():
    score = 0
    for question, options in quiz_questions.items():
        print("\n" + question)
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")
        while True:
            try:
                answer = int(input("Enter the option number: "))
                if 1 <= answer <= len(options):
                    selected = options[answer - 1]
                    if selected == correct_answers[question]:
                        print("Correct!\n")
                        score += 1
                    else:
                        print(f"Wrong. Correct answer: {correct_answers[question]}\n")
                    break
                else:
                    print(f"Please enter a number between 1 and {len(options)}")
            except ValueError:
                print("Please enter a valid number.")
    print(f"Quiz finished! Your score is {score}/{len(quiz_questions)}\n")
    return score

def Display_Score(score):
    print(f"\nYour most recent quiz score: {score}/{len(quiz_questions)}\n")
    input("Press Enter to return to the menu.")
    Option_Select(score)

def Quit_Quiz():
    print("Thanks for playing the quiz. Goodbye!")
    exit()

def User_Age():
    while True:
        try:
            user_age = int(input("Please enter your age: "))
            if user_age > MAX_AGE:
                print("You are no longer doing NCEA, and do not require my quiz.")
                break
            elif 0 < user_age < MIN_AGE:
                print("You are too young to use this quiz.")
                break
            elif user_age <= 0:
                print("Enter an integer above 0")
            else:
                Option_Select(0)
                break
        except ValueError:
            print("Please enter an integer.")
            
def Quiz_Description():
    with open('Description.txt', 'r') as f:
        description = f.read()
        print(description)
    input("\nType anything to continue: ")
    User_Age()

def Option_Select(current_score):
    print("\n1. Play Quiz\n2. View Score\n3. Quit")
    while True:
        try:
            user_option = int(input("Enter an option: "))
            if user_option == 1:
                new_score = Play_Quiz()
                Option_Select(new_score)
                break
            elif user_option == 2:
                Display_Score(current_score)
                break
            elif user_option == 3:
                Quit_Quiz()
                break
            else:
                print("Please enter an integer between 1 - 3")
        except ValueError:
            print("Please enter a valid integer.")

Quiz_Description()
print("Goodbye!")
