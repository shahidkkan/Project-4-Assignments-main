import random
def guess_game():
    print("Guess My Number")
    computer_gen = random.randint(0,10)

    while True:
     my_guess = int(input("I am thinking of a number between 0 and 99... Enter a guess: "))
     if my_guess == computer_gen:
         print(f"Congrats! The number was: {my_guess} ")
         break
     elif my_guess > computer_gen:
         print("Your guess is too high")
     elif my_guess < computer_gen:
         print("Your guess is too low")
         

guess_game()