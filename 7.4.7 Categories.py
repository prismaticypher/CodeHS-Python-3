categories = {}

for _ in range(3):
    category = input("Enter a category: ")
    items = []
    for _ in range(3):
        item = input(f"Enter something in that category: ")
        items.append(item)
    categories[category] = items
for category, items in categories.items():
    print(f"{category}: {' '.join(items)}")