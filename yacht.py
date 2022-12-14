# The dice game Yacht is from the same family as Poker Dice, Generala and particularly Yahtzee, of which it is a precursor. 
# In the game, five dice are rolled and the result can be entered in any of twelve categories. 
# The score of a throw of the dice depends on category chosen.

# Given a list of values for five dice and a category, your solution should return the score of the dice for that category.
# If the dice do not satisfy the requirements of the category your solution should return 0. You can assume that five values 
# will always be presented, and the value of each will be between one and six inclusively. You should not assume that the dice are ordered.

def score(dice, category):
    total = 0
    if category == YACHT:
        total += 50 if len(set(dice)) == 1 else 0
    elif category in {ONES, TWOS, THREES, FOURS, FIVES, SIXES}:
        total += category * sum(throw == category for throw in dice)
    elif category == FULL_HOUSE:
        total += sum(dice) if set(Counter(dice).values()) == {2, 3} else 0
    elif category == FOUR_OF_A_KIND:
        side, times = Counter(dice).most_common(1)[0]
        total += 4 * side if times in [4, 5] else 0
    elif category == LITTLE_STRAIGHT:
        total += 30 if set(dice) == {1, 2, 3, 4, 5} else 0
    elif category == BIG_STRAIGHT:
        total += 30 if set(dice) == {2, 3, 4, 5, 6} else 0
    elif category == CHOICE:
        total += sum(dice)
    else:
        raise ValueError(f"unknown category: {category}")
    return total
