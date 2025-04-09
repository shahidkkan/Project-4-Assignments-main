import random
secrate = random.randint(0,10)
print("Guess My Number")
print("I am thinking of a number between 0 and 10...")
user_guess = int(input("Enter a guess: "))
while True:
    if user_guess > secrate:
        print("Your guess is too high")
    elif user_guess < secrate:
        print("Your guess is too low")
    elif user_guess == secrate:
        print(f"Congrats! The number was: {user_guess}")
        break
    user_guess = int(input("Enter a Number: "))