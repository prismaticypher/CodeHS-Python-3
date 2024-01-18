# Write your function for converting Celsius to Fahrenheit here.
# Make sure to include a comment at the top that says what
# each function does!
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


# Now change 0C to F:
print(celsius_to_fahrenheit(0))

# Change 100C to F:
print(celsius_to_fahrenheit(100))


# Change 40F to C:
print(fahrenheit_to_celsius(40))

# Change 80F to C:
print(fahrenheit_to_celsius(80))