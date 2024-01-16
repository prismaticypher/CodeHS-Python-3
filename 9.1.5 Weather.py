def suggest_sandals():
    print("On a sunny day, sandals are appropriate footwear.")

def suggest_galoshes():
    print("On a rainy day, galoshes are appropriate footwear.")

def suggest_boots():
    print("On a snowy day, boots are appropriate footwear.")

def suggest_invalid():
    print("Invalid option. Please choose from sunny, rainy, or snowy.")

weather = input("What is the weather? (sunny, rainy, snowy): ")
    
if weather.lower() == "sunny":
    suggest_sandals()
elif weather.lower() == "rainy":
    suggest_galoshes()
elif weather.lower() == "snowy":
    suggest_boots()
else:
    suggest_invalid()