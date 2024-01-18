def add_numbers(x, y):
    return x + y

def subtract_numbers(x, y):
    return x - y

def multiply_numbers(x, y):
    return x * y

num1 = int(input("What is the first number?: "))
num2 = int(input("What is the second number?: "))
operation = input("Choose an operation (add, subtract, multiply): ")

if operation == "add":
    result = add_numbers(num1, num2)
    print(f"{num1} + {num2} = {result}")
elif operation == "subtract":
    result = subtract_numbers(num1, num2)
    print(f"{num1} - {num2} = {result}")
elif operation == "multiply":
    result = multiply_numbers(num1, num2)
    print(f"{num1} * {num2} = {result}")
else:
    print("Invalid operation. Please choose add, subtract, or multiply.")