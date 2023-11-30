number_of_names = int(input("How many names do you have? "))
total_names = ""

for i in range(number_of_names):
    name = input("Enter your name(s): ")
    total_names += " " + name 

print(f"Your full name is{total_names}.")