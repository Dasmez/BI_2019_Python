def checkio(a: list) -> list:
    b = []
    for element in a:
        if a.count(element) != 1:
            b.append(element)
    return b
