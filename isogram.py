# Determine if a word or phrase is an isogram.
# An isogram (also known as a "non-pattern word") is a word or phrase without a repeating letter,
# however spaces and hyphens are allowed to appear multiple times.

# Examples of isograms:
## lumberjacks
## background
## downstream
## six-year-old

from string import ascii_lowercase as alphabet


def is_isogram(phrase):
    phrase = phrase.lower()
    letters = [letter for letter in phrase if letter in alphabet]
    return len(set(letters)) == len(letters)
