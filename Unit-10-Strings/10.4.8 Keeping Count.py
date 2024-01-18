# update this function to return the number of times `second` appears in `first`!
def count_occurrences(word, character):
    count = 0
    for char in word:
        if char == character:
            count += 1
    return count