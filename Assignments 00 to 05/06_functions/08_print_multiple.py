def print_multiple(message, times):
    for i in range(times):
        print(message)

def main():
    msg = input("Enter a message: ")
    times = int(input("How many times do you want to print it? "))
    print_multiple(msg, times)
    
if __name__ == "__main__":
    main()