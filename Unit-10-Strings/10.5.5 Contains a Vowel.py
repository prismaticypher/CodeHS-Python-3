# use `in` to determine if `word` contains any vowels!
def contains_vowel(word):
    vowels = "aeiou"
    return any(char in vowels for char in word)