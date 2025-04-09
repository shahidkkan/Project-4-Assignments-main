import random

DONE_LIKELIHOOD = 0.3

def Done():
    return random.random() < DONE_LIKELIHOOD

def chaotic_counting():
    for i in range(1, 10):
        if Done():
           return
        print(i,end=" ")
def main():
        print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
        chaotic_counting()
        print("\nI'm done.")
main()
