# Given any two lists A and B, determine if:
  # List A is equal to list B; or
  # List A contains list B (A is a superlist of B); or
  # List A is contained by list B (A is a sublist of B); or
  # None of the above is true, thus lists A and B are unequal

  # Specifically, list A is equal to list B if both lists have the same values in the same order. 
# List A is a superlist of B if A contains a sub-sequence of values equal to B. 
# List A is a sublist of B if B contains a sub-sequence of values equal to A.

"""This exercise stub and the test suite contain several enumerated constants."""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = None
SUPERLIST = None
EQUAL = None
UNEQUAL = None

def sublist(list_one, list_two):
    if list_one == list_two:
        return None

    if list_one.sort() != list_two.sort():
        return False

    for num in list_one:
        if num in list_two == list_one:
            return True

        elif list_one == list_two:
            return True
        else:
            return None
        
   
