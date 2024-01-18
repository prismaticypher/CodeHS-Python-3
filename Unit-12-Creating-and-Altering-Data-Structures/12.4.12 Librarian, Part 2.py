last_names = []

for _ in range(5):
    full_name = input("Name: ")
    last_name = full_name.split()[-1]
    last_names.append(last_name)

last_names.sort()
print(last_names)