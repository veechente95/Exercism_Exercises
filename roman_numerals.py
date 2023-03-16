# Write a function to convert from normal numbers to Roman Numerals.

def roman(number):
    num = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    letters = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    roman_numeral = ""
    current_number = number
    position = 0

    while current_number > 0:
        if current_number - num[position] >= 0:
            roman_numeral += letters[position]
            current_number -= num[position]
        else:
            position += 1

    return roman_numeral
