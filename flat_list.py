def flat_list(array):
    c = []
    for element in array:
        if type(element) is list:
            c += flat_list(element)
        else:
            c.append(element)
    return c
