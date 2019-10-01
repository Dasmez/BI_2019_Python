def flat_list(array):
    c = []
    for element in array:
        if type(element) is list:
            c = c + flat_list(array[i])
        else:
            c.append(array[i])
    return (c)
