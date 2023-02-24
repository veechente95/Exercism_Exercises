"""Functions to help edit essay homework using string manipulation."""


def capitalize_title(title):
    """Convert the first letter of each word in the title to uppercase if needed."""
    return title.title()


def check_sentence_ending(sentence):
    """Check the ending of the sentence to verify that a period is present."""
    if sentence[-1] == ".":
        return True
    else:
        return False


def clean_up_spacing(sentence):
    """Verify that there isn't any whitespace at the start and end of the sentence."""
    return sentence.strip()
    

def replace_word_choice(sentence, old_word, new_word):
    """Replace a word in the provided sentence with a new one."""
    new_word = sentence.replace(old_word, new_word)
    return new_word
    
    
