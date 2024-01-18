# update the function body to return `string`, but with the character at
# `index` replaced by `letter`
def replace_at_index(string, index, letter):
    return string[:index] + letter + string[index + 1:]