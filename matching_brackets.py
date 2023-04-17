# Given a string containing brackets [], braces {}, parentheses (), or any combination thereof, 
# verify that any and all pairs are matched and nested correctly. The string may also contain other 
# characters, which for the purposes of this exercise should be ignored.

def is_paired(input_string):
    opened = "[{("
    closed = "]})"
    stack = []
    for char in input_string:
        if char in opened:
            stack.append(char)
        elif char in closed:
            if not stack or opened[closed.index(char)] != stack.pop():
                return False
    return not stack
