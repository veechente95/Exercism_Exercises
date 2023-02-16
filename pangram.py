# Determine if a sentence is a pangram. A pangram is a sentence using every letter of the alphabet at least once. 
# The best known English pangram is: The quick brown fox jumps over the lazy dog.
# The alphabet used consists of letters a to z, inclusive, and is case insensitive.

def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    for letter in alphabet:
        if letter not in sentence.lower():
            return False

    if letter in alphabet:
        return True
