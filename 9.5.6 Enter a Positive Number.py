def retrieve_positive_number():
    while True:
        try:
            user_input = float(input("Enter a positive number: "))
            if user_input > 0:
                return user_input
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

result = retrieve_positive_number()
print(f"You entered a positive number: {result}")