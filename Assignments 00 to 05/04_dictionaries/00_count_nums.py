def get_user_numbers():
     """
     Create an empty list.
     Ask the user to input numbers and store them in a list. 
     Once they enter a blank line, break out of the loop and return the list.
    """
     user_number = []
     while True:
          user_input = input("Enter a Number: ")

          if user_input == "":
               break
          
          user_input = int(user_input)
          user_number.append(user_input)
     return user_number

def count_num(num_lst):
     """
    Create an empty dictionary.
    Loop over the list of numbers. 
    If the number is not in the dictionary, add it as a key with a value of 1.
    If the number is in the dictionary, increment its value by 1.
    """
     num_dic = {}

     for num in num_lst:
          if num not in num_dic:
               num_dic[num] = 1
          else:
               num_dic[num] += 1
     return num_dic

def print_counts(num_dic):
      """
    Loop over the dictionary and print out each key and its value.
    """
      for num in num_dic:
           print(f"{num} appears {num_dic[num]} times")
          
def main():
     user_number =  get_user_numbers()
     num_dict = count_num(user_number)
     print_counts(num_dict)
main() 