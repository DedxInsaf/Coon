def find_max(*args):
    if len(args) == 0:
        raise TypeError("find_max expected at least 1 argument, got 0")
    max_value = args[0]
    for elem in args[1:]:
        if elem > max_value:
            max_value = elem

    return max_value
