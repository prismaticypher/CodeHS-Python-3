numbers = []

for _ in range(5):
    num = int(input("Number: "))
    numbers.append(num)
    print(numbers)

sum_of_numbers = sum(numbers)
print(f'Sum: {sum_of_numbers}')