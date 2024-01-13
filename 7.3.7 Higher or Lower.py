magic_number = 3

# Your code here...
while True:
    user_input = int(input("Enter a guess: "))
    if user_input < magic_number:
        print("Too low!")
    elif user_input > magic_number:
        print("Too high!")
    else:
        print("Correct!")
        break