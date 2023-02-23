def get_rounds(number):
    """Create a list containing the current and next two round numbers."""
    return[number, number + 1, number + 2]
    

def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers."""
    new_list = rounds_1 + rounds_2
    return new_list


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number."""
    if number in rounds:
        return True
    else:
        return False


def card_average(hand):
    """Calculate and returns the average card value from the list."""
    num_cards = len(hand)
    sum_cards = sum(hand)
    average = sum_cards / num_cards
    return average


def approx_average_is_average(hand):
    """Return if an average is using (first + last index values ) OR ('middle' card) == calculated average."""
    avg = card_average(hand)
    middle = hand[len(hand)//2]
    if ((hand[0] + hand[-1]) / 2) == avg or (middle == avg):
        return True
    else:
        return False


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    pass


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    pass
