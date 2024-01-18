# Initialize an empty list to store last names
last_names = []

# Use a for loop to get last names from the user
for _ in range(5):
    last_name = input("Name: ")
    last_names.append(last_name)

# Sort the list of last names
sorted_last_names = sorted(last_names)

# Print the sorted list of last names
print(sorted_last_names)