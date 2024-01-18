num_names = int(input("Number of names: "))

names = []

for _ in range(num_names):
    name = input("Name: ")
    names.append(name)

first_name = names[0]
middle_names = names[1:-1]
last_name = names[-1]

print(f'First name: {first_name}')

if middle_names:
    print(f'Middle names: {middle_names}')
else:
    print('Middle names: []')

print(f'Last name: {last_name}')