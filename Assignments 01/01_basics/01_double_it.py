def double():
    num = int(input("Enter a number: "))
    while num < 100:
        doubled = num * 2
        print(f"Double of {num} is {doubled}")
        num += num
        
double()
