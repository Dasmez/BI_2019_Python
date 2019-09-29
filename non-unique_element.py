def checkio(a: list) -> list:
    b = []
    for i in range(len(a)):
        if a.count(a[i]) != 1:
            b.append(a[i])
    return (b)
