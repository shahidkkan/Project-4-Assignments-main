# 📌 File Handling Tasks in Python
# 👶 Beginner Task:
# 📝 Task 1: Write & Read a File

# data.txt naam ki file create karo.

# Usme 3 lines likho.

# File ko close karo.

# Phir usi file ko open karke read karo aur terminal par print karo.
file = "data.txt"
with open(file,"w") as file:
    file.writelines(["Hello This Is One Line\n","Welcome to the python Programming\n","This is Thired Line"])
    
    
    
with open("data.txt","r") as file:
    lines = file.readlines()
    for line in lines:
        print(line)