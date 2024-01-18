def remove_all_from_string(word, substring):
    while substring in word:
        index = word.find(substring)
        word = word[:index] + word[index + len(substring):]
    return word

word = input("Enter the main string: ")
substring = input("Enter the substring to remove: ")

result = remove_all_from_string(word, substring)
print(result)