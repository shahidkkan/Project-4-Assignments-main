def main():
    fahrenheit = int(input("Enter temperature in Fahrenheit "))
    celsius = (fahrenheit - 32) * 5.0 / 9.0 
    print(f"Temperature {fahrenheit}F = {celsius}C")
main()
