def owl_count(text):
    # Convert the text to lowercase and split into words
    words = text.lower().split()

    # List to store indices of words containing "owl"
    indices = [index for index, word in enumerate(words) if "owl" in word]

    # Count the words containing "owl"
    count = len(indices)

    print(f'There {"was" if count == 1 else "were"} {count} {"word" if count == 1 else "words"} that contained "owl".')

    if count > 0:
        print(f'They occurred at indices: {indices}')

    return count

# Get user input
user_text = input("Enter some text: ")

# Call the function
owl_count(user_text)