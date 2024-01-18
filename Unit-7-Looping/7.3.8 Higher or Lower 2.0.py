my_float = 3.3312

# Your code here...
while True:
    user_input = float(input("Enter a guess: "))
    user_input = round(float(user_input), 2)
    my_float = round(float(my_float), 2)
    if user_input < my_float:
        print("Too low!")
    elif user_input > my_float:
        print("Too high!")
    else:
        print("Correct!")
        break