def flat_list(array):
    c = []
    for i in range(len(array)):
        if type(array[i]) == list:
            c = c + flat_list(array[i])
        else:
            c.append(array[i])
    array = c
    return (array)
