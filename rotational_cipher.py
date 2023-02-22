alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"


def rotate(text, shift_amount):
    lower = alphabet.lower()
    upper = alphabet.upper()
    result = ''
    for char in text:
        if char.isalpha():
            if char.islower():
                result += lower[lower.index(char) + shift_amount]
            else:
                result += upper[upper.index(char) + shift_amount]
        else:
            result += char
    return result
