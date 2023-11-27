age = int(input("Age: "))
citizenship = input("Born in the U.S.? (Yes/No): ").lower()
residency = int(input("Years of Residency: "))


if age >= 35 and (citizenship == "yes") and residency >= 14:
    print ("You are eligible to run for president.")
else:
    print ("You are not eligible to run for president.")
    
if age < 35:
    print("You are too young. You must be at least 35 years old.")
    
if citizenship == "no":
    print ("You must be born in the U.S. to run for president.")
    
if residency < 14:
    print ("You have not been a resident for long enough.")