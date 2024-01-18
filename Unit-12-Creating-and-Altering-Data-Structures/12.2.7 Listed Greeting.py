# fill in this function to greet the user!
def greeting(user_info):
    info_list = user_info.split()

    name = info_list[0]
    hobby = ' '.join(info_list[2:])

    return f'Hello, {name}! I also enjoy {hobby}!'