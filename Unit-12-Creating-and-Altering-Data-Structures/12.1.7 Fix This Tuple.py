my_tuple = (0, 1, 2, "hi", 4, 5)

# Your code here...

index_of_hi = my_tuple.index("hi")
new_tuple = my_tuple[:index_of_hi] + (3,) + my_tuple[index_of_hi + 1:]

print(new_tuple)