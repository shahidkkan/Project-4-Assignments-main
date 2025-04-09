def read_phone_number():
    """
    Ask the user for names/numbers to story in a phonebook (dictionary).
    Returns the phonebook.
    """
    phonebook = {}

    while True:
        name = input("Name: ")
        if name == "":
            break
        number = input("Number: ")
        
        phonebook[name] = number
    return phonebook
def print_phonebook(phonebook):
      """
    Prints out all the names/numbers in the phonebook.
    """
      for name in phonebook:
           print(f"{name} -> {phonebook[name]}")

def lookup_numbers(phonebook): 
      """
    Allow the user to lookup phone numbers in the phonebook
    by looking up the number associated with a name.
    """
      while True:
         lookup = input("Enter name to lookup: ")
         if lookup == "":
              break
         
         if lookup not in phonebook:
              print(f"{lookup} is not in the phonebook")
         else:
              print(phonebook[lookup])




phonebook = read_phone_number()
print_phonebook(phonebook)
lookup_numbers(phonebook)