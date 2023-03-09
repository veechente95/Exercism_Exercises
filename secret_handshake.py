def commands(binary_str):
    empty_list = []

    if binary_str[-1] == '1':
        empty_list.extend(["wink"])
    if binary_str[-2] == '1':
        empty_list.extend(["double blink"])
    if binary_str[-3] == '1':
        empty_list.extend(["close your eyes"])
    if binary_str[-4] == '1':
        empty_list.extend(["jump"])
    if binary_str[-5] == '1':
        empty_list.reverse()

    return empty_list
