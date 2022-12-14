# The dice game Yacht is from the same family as Poker Dice, Generala and particularly Yahtzee, of which it is a precursor. 
# In the game, five dice are rolled and the result can be entered in any of twelve categories. 
# The score of a throw of the dice depends on category chosen.

# Given a list of values for five dice and a category, your solution should return the score of the dice for that category.
# If the dice do not satisfy the requirements of the category your solution should return 0. You can assume that five values 
# will always be presented, and the value of each will be between one and six inclusively. You should not assume that the dice are ordered.

# Score categories.
# Change the values as you see fit.
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    for number in dice:
        counts = [dice.count(number)]
    if category == YACHT:
        return 50 * (5 in counts)
    if category < FULL_HOUSE: #ONES - SIXES
        return category * dice.count(category)
    if category == FULL_HOUSE:
        return sum(dice) * (3 in counts and 2 in counts)
    if category == FOUR_OF_A_KIND:
        return sorted([number if dice.count(number) > 3 else 0 for number in dice])[-1]*4
    if category == LITTLE_STRAIGHT:
        return 30 * (all([count == 1 for count in counts]) and 6 not in dice)
    if category == BIG_STRAIGHT:
        return 30 * (all([count == 1 for count in counts]) and 1 not in dice)
    if category == CHOICE:
        return sum(dice)
    return 0
