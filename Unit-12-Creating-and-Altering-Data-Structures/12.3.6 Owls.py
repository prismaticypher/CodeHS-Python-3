# this function should return the number of words that contain "owl"!
def owl_count(text):
    # Convert the text to lowercase and split into words
    words = text.lower().split()

    # Count the words containing "owl"
    count = sum("owl" in word for word in words)

    return count