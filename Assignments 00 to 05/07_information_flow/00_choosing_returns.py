ADULT_AGE = 18
def is_adult(age):
    return age >= ADULT_AGE
age = int(input("How old are you? "))
print(is_adult(age))