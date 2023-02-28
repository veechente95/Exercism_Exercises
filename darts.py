def score(x, y):
    throw = (x**2) + (y**2)
    if throw > 100:
        return 0
    elif throw > 25:
        return 1
    elif throw > 1:
        return 5
    else:
        return 10
