status = input("Are you an administrator, teacher, or student?: ").lower()

if (status == "teacher") or (status == "administrator"):
    print("Administrators and teachers get keys!")

elif (status == "student"):
    print("Students do not get keys!")
    
else:
    print("You can only be an administrator, teacher, or student!")