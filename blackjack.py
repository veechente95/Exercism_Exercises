"""Functions to help play and score a game of blackjack."""

def value_of_card(card):
    """Determine the scoring value of a card."""
    if card in "JQK":
        return 10
    if card == "A":
        return 1
    else:
        return int(card)

    
def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand."""
    if value_of_card(card_one) > value_of_card(card_two):
        return card_one
    if value_of_card(card_one) == value_of_card(card_two):
        return card_one, card_two
    else:
        return card_two

    
def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card."""
    if card_one == "A" or card_two == "A":
        return 1
    if value_of_card(card_one) + value_of_card(card_two) <= 10:
        return 11
    else:
        return 1


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'."""
    if card_one == "A" and value_of_card(card_two) == 10 or card_two == "A" and value_of_card(card_one) == 10:
        return True
    else:
        return False
        

def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands."""
    if value_of_card(card_one) == value_of_card(card_two):
        return True
    else:
        return False


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet."""
    if 9 <= (value_of_card(card_one) + value_of_card(card_two)) <= 11:
        return True
    else:
        return False
