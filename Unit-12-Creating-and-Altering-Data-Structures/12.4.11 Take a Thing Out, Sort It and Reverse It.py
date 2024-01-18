def remove_sort_reverse(my_list):
    my_list = [item for item in my_list if item != "eggplant"]
    my_list.sort()
    my_list.reverse()

    return my_list