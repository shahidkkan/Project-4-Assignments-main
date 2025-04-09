def print_divisor(num):
     for i in range(num):
         curr_devisor = i + 1
         if num % curr_devisor == 0:
             print(curr_devisor, end=' ')
            
def main():
    num = int(input("Enter a number: "))
    print_divisor(num)

if __name__ == "__main__":
    main()