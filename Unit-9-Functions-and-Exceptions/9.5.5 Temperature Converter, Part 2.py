def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

try:
    celsius_input = float(input("Enter temperature in Celsius: "))
    fahrenheit_result = celsius_to_fahrenheit(celsius_input)
    print(f"{celsius_input} degrees Celsius is {fahrenheit_result:.2f} degrees Fahrenheit.")
except ValueError:
    print("Invalid input. Please enter a valid number.")

try:
    fahrenheit_input = float(input("Enter temperature in Fahrenheit: "))
    celsius_result = fahrenheit_to_celsius(fahrenheit_input)
    print(f"{fahrenheit_input} degrees Fahrenheit is {celsius_result:.2f} degrees Celsius.")
except ValueError:
    print("Invalid input. Please enter a valid number.")