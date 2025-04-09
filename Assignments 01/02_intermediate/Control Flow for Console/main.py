import random
Num_Rounds = 5
def highe_low_game():
    score = 0
    print("Welcome to the High-Low Game!")
    print("-"*20)
    
    for round_nums in range(1,Num_Rounds + 1):
        print(f"Round {round_nums}")
        user_num = random.randint(1,100)
        computer_num = random.randint(1,100)
        print(f"You Number is {user_num}")
        
        while True:
          user_guess = input("Do you think your number is higher or lower than the computer's? (higher/lower): ").strip().lower()
          if user_guess in ["higher","lower"]:
              break
          else:
              print("Please enter either 'higher' or 'lower'")
              
        if (user_guess == "higher" and user_num > computer_num) or (user_guess == "lower" and user_num < computer_num):
            print(f"You were right! The computer's number was {computer_num}")
            score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_num}")      
        print(f"Your score is now {score}")
    print("Thanks for playing!")
    
    if score == Num_Rounds:
        print("Wow! You played perfectly! 🎉")
    elif score >= Num_Rounds //2:
        print("Good job, you played really well! 👍")
    else:
        print("Better luck next time! 😢")

highe_low_game()