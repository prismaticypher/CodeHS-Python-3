def get_index(word):
    while True:
        try:
            index = int(input("Enter an index (-1 to quit): "))
            if index == -1:
                return -1
            if 0 <= index < len(word):
                return index
            else:
                print("Invalid index")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_letter():
    while True:
        letter = input("Enter a letter: ")
        if len(letter) == 1 and 'a' <= letter <= 'z':
            return letter
        elif len(letter) != 1:
            print("Must be exactly one character!")
        else:
            print("Character must be a lowercase letter!")

def main():
    initial_word = input("Enter a word: ")
    current_word = list(initial_word)

    while True:
        index = get_index(current_word)
        if index == -1:
            break

        letter = get_letter()
        current_word[index] = letter

        print(''.join(current_word))

if __name__ == "__main__":
    main()
