# your function should return the maximum value in `my_list`
def max_int_in_list(my_list):
    max_int = my_list[0]

    for num in my_list:
        if num > max_int:
            max_int = num

    return max_int