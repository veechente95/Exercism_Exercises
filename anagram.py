def find_anagrams(word, candidates):
    for letters in candidates:
        if sorted(word.lower()) == sorted(letters.lower()) and word.lower() != letters.lower():
            return [letters]
