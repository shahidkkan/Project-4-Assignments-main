def greetings(name:str) -> str:
    return f"Greetings {name}"
name = input("What is your name? ")
print(greetings(name))