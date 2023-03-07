# Given any two lists A and B, determine if:
  # List A is equal to list B; or
  # List A contains list B (A is a superlist of B); or
  # List A is contained by list B (A is a sublist of B); or
  # None of the above is true, thus lists A and B are unequal

  # Specifically, list A is equal to list B if both lists have the same values in the same order. 
# List A is a superlist of B if A contains a sub-sequence of values equal to B. 
# List A is a sublist of B if B contains a sub-sequence of values equal to A.

"""This exercise stub and the test suite contain several enumerated constants."""
SUBLIST = "sublist"
SUPERLIST = "superlist"
EQUAL = "equal"
UNEQUAL = "unequal"


def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL    
    elif len(list_one) > len(list_two):
        bigger = list_one
        smaller = list_two
    else:
        bigger = list_two
        smaller = list_one
    
    for i in range(len(bigger)):
        if bigger[i:i + len(smaller)] == smaller and bigger == list_one:
            return SUPERLIST
        elif bigger[i:i + len(smaller)] == smaller and bigger == list_two:
            return SUBLIST
    return UNEQUAL
