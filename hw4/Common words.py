def checkio(first, second):
    result = []
    first = first.split(",")
    second = second.split(",")
    first = set(first)
    second = set(second)
    result = set.intersection(first, second)
    a = sorted(result)
    return ",".join(a)

