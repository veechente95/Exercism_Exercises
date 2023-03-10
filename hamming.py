def distance(strand_a, strand_b):
    for letter in strand_a and strand_b:
        if letter != letter:
            return letter.count(letter)
