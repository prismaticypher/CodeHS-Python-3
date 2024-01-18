# Use a while loop here to repeatedly ask the user for
# a denominator for as long as the denominator is 0
# (or, put another way, until the denominator is not
# equal to 0).

numerator = int(input("Enter a numerator: "))

while True:
    denominator = int(input("Enter denominator: "))
    
    if denominator == 0:
        print("Cannot divide by zero. Please enter a non-zero denominator.")
    else:
        break

if int(numerator / denominator) * denominator == numerator:
    print("Divides evenly!")
else:
    print("Doesn't divide evenly.")
