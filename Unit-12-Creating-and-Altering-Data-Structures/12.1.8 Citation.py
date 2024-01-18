# fill in the `citation` function to return the author's name in the correct format
def citation(author_name):
    last_name, first_name, middle_name = author_name

    formatted_name = f"{middle_name}, {last_name} {first_name}"

    return formatted_name