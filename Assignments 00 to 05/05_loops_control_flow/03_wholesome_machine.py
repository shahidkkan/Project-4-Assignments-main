AFFIRMATION = "You are doing great! Keep it up!"
def wholesome_machine():
    print(f"Please type the following affirmation {AFFIRMATION}:")
    while True:
     user_input = input()
     if user_input == AFFIRMATION:
         print("Great job! You are doing amazing!")
         break
     else:
         print("That's okay! Just keep trying!")
wholesome_machine()