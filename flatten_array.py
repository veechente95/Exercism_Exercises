def flatten(iterable):
    for num in iterable:
        if num == "null":
            pass
    return [item for sublist in iterable for item in sublist] 
