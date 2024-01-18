"""
This program asks the user for three ingredients,
three amounts, and a number of servings, and
determines how much of each ingredient is needed
to serve the specified number of servings.
"""

ingredient1 = input("Enter ingredient 1: ")
ounce1 = float(input(f"Ounces of {ingredient1}?: "))

ingredient2 = input("Enter ingredient 1: ")
ounce2 = float(input(f"Ounces of {ingredient2}?: "))

ingredient3 = input("Enter ingredient 1: ")
ounce3 = float(input(f"Ounces of {ingredient3}?: "))

servings = int(input("Number of servings: "))

print(f"Total ounces of {ingredient1}: {ounce1 * servings}")
print(f"Total ounces of {ingredient2}: {ounce2 * servings}")
print(f"Total ounces of {ingredient3}: {ounce3 * servings}")