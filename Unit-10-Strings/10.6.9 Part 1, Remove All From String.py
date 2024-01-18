# update the function to return `word` with all instances of `letter` removed!
def remove_all_from_string(word, letter):
    while letter in word:
        index = word.find(letter)
        word = word[:index] + word[index + 1:]
    return word