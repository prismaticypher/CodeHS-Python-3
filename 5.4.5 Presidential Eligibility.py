age = int(input("Age: "))
citizenship = input("Born in the U.S.? (Yes/No): ").lower()
residency = int(input("Years of Residency: "))

if age >= 35 and (citizenship == "yes") and residency >= 14:
    print ("You are eligible to run for president.")
else:
    print ("You are not eligible to run for president.")