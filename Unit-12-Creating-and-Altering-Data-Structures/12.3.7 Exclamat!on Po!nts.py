# update this function so it replaces all lowercase 'i's in `text` with '!'
def exclamation(text):
    text_list = list(text)

    for i in range(len(text_list)):
        if text_list[i] == 'i':
            text_list[i] = '!'

    result = ''.join(text_list)

    return result