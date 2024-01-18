def authenticate_password(correct_password, max_attempts):
    attempts = 0

    while attempts < max_attempts:
        user_password = input("Enter your password: ")
        if user_password == correct_password:
            print("Correct password! Access granted.")
            break
        else:
            attempts += 1
            print("Incorrect password. Please try again.")

    if attempts == max_attempts:
        print("Incorrect password. Maximum number of attempts reached. Access denied.")

correct_password = "password123"
max_attempts = 3

print("Password Authentication Program")
authenticate_password(correct_password, max_attempts)