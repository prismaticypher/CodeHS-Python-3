def calculate_area(side_length=10):
    area = side_length ** 2
    print(f"The area of a square with sides of length {side_length} is {area}.")

user_length = float(input("Enter side length: "))
    
if user_length <= 0:
    calculate_area()
else:
    calculate_area(user_length)