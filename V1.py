MAX_AGE = 18
MIN_AGE = 12

def Play_Quiz():
    

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
                Option_Select()
                break
        except ValueError:
            print("Please enter an integer.")


def Quiz_Description():
    with open('Description.txt','r')as f:
        Description = f.read()
        print(Description)
        input("\nType anything to continue: ")
    User_Age()

def Option_Select():
    print("1. Play Quiz\n2. View Score\n3. Quit")
    while True:
        try:
            user_option = int(input("Enter an option: "))
            if user_option > 3:
                print("Please enter an integer between 1 - 3")
            elif user_option <= 0:
                print("Please enter an integer between 1 - 3")
        except ValueError:
            print("Please enter an integer between 1 - 3")
        if user_option == 1:
            Play_Quiz()
        elif user_option == 2:
            Display_Score()
        elif user_option == 3:
            Quit_Quiz()
            
Quiz_Description()
print("Goodbye!")